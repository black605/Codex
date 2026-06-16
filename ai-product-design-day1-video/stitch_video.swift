import AppKit
import AVFoundation
import CoreVideo
import Foundation

let args = CommandLine.arguments
guard args.count >= 3 else {
    fputs("Usage: swift stitch_video.swift <input-dir> <output-file>\n", stderr)
    exit(1)
}

let inputDir = URL(fileURLWithPath: args[1], isDirectory: true)
let outputURL = URL(fileURLWithPath: args[2])

let fps = 30
let secondsPerSlide = 4
let framesPerSlide = fps * secondsPerSlide

let fileManager = FileManager.default
let imageFiles = (try fileManager.contentsOfDirectory(at: inputDir, includingPropertiesForKeys: nil))
    .filter { $0.pathExtension.lowercased() == "png" }
    .sorted { $0.lastPathComponent < $1.lastPathComponent }

guard let firstImage = NSImage(contentsOf: imageFiles[0]),
      let firstRep = NSBitmapImageRep(data: firstImage.tiffRepresentation!) else {
    fputs("Unable to read first image.\n", stderr)
    exit(1)
}

let width = firstRep.pixelsWide
let height = firstRep.pixelsHigh

if fileManager.fileExists(atPath: outputURL.path) {
    try? fileManager.removeItem(at: outputURL)
}

let writer = try AVAssetWriter(outputURL: outputURL, fileType: .mp4)
let settings: [String: Any] = [
    AVVideoCodecKey: AVVideoCodecType.h264,
    AVVideoWidthKey: width,
    AVVideoHeightKey: height,
]

let writerInput = AVAssetWriterInput(mediaType: .video, outputSettings: settings)
writerInput.expectsMediaDataInRealTime = false

let attributes: [String: Any] = [
    kCVPixelBufferPixelFormatTypeKey as String: Int(kCVPixelFormatType_32ARGB),
    kCVPixelBufferWidthKey as String: width,
    kCVPixelBufferHeightKey as String: height,
]

let adaptor = AVAssetWriterInputPixelBufferAdaptor(assetWriterInput: writerInput, sourcePixelBufferAttributes: attributes)

guard writer.canAdd(writerInput) else {
    fputs("Cannot add writer input.\n", stderr)
    exit(1)
}

writer.add(writerInput)
writer.startWriting()
writer.startSession(atSourceTime: .zero)

func pixelBuffer(from image: NSImage, width: Int, height: Int) -> CVPixelBuffer? {
    var pxbuffer: CVPixelBuffer?
    let status = CVPixelBufferCreate(kCFAllocatorDefault, width, height, kCVPixelFormatType_32ARGB, nil, &pxbuffer)
    guard status == kCVReturnSuccess, let buffer = pxbuffer else {
        return nil
    }

    CVPixelBufferLockBaseAddress(buffer, [])
    defer { CVPixelBufferUnlockBaseAddress(buffer, []) }

    guard let context = CGContext(
        data: CVPixelBufferGetBaseAddress(buffer),
        width: width,
        height: height,
        bitsPerComponent: 8,
        bytesPerRow: CVPixelBufferGetBytesPerRow(buffer),
        space: CGColorSpaceCreateDeviceRGB(),
        bitmapInfo: CGImageAlphaInfo.noneSkipFirst.rawValue
    ) else {
        return nil
    }

    let graphicsContext = NSGraphicsContext(cgContext: context, flipped: false)
    NSGraphicsContext.saveGraphicsState()
    NSGraphicsContext.current = graphicsContext
    context.clear(CGRect(x: 0, y: 0, width: width, height: height))
    if let cgImage = image.cgImage(forProposedRect: nil, context: nil, hints: nil) {
        context.draw(cgImage, in: CGRect(x: 0, y: 0, width: width, height: height))
    }
    NSGraphicsContext.restoreGraphicsState()

    return buffer
}

let queue = DispatchQueue(label: "video.queue")
let group = DispatchGroup()
group.enter()

var frameCount = 0

writerInput.requestMediaDataWhenReady(on: queue) {
    outerLoop: for imageURL in imageFiles {
        guard let image = NSImage(contentsOf: imageURL),
              let buffer = pixelBuffer(from: image, width: width, height: height) else {
            continue
        }

        for _ in 0..<framesPerSlide {
            while !writerInput.isReadyForMoreMediaData {
                Thread.sleep(forTimeInterval: 0.01)
            }

            let time = CMTime(value: CMTimeValue(frameCount), timescale: CMTimeScale(fps))
            if !adaptor.append(buffer, withPresentationTime: time) {
                fputs("Failed to append frame at \(frameCount).\n", stderr)
                writerInput.markAsFinished()
                writer.cancelWriting()
                group.leave()
                break outerLoop
            }
            frameCount += 1
        }
    }

    writerInput.markAsFinished()
    writer.finishWriting {
        if writer.status == .completed {
            print("Video written to \(outputURL.path)")
        } else {
            fputs("Video export failed: \(writer.error?.localizedDescription ?? "unknown error")\n", stderr)
        }
        group.leave()
    }
}

group.wait()
