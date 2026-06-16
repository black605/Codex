from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


WIDTH = 720
HEIGHT = 1280
BG_TOP = (249, 244, 233)
BG_BOTTOM = (255, 255, 255)
ACCENT = (222, 78, 54)
TEXT = (30, 34, 44)
MUTED = (91, 99, 112)
CARD = (255, 255, 255)
CARD_BORDER = (235, 226, 212)

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "renders"
OUT.mkdir(exist_ok=True)

FONT_PATH = "/System/Library/Fonts/PingFang.ttc"


SCENES = [
    {
        "label": "AI产品设计 · Day 1",
        "title": "第一天先建立整体认知",
        "subtitle": "不要一上来钻模型细节，先弄清楚 AI 产品到底在解决什么问题。",
        "bullets": [
            "理解什么是 AI 产品设计",
            "分清它和传统产品设计的区别",
            "记住 AI 产品的最小结构",
        ],
        "footer": "今天的关键词：用户任务 / AI能力 / 交互闭环 / 容错机制",
    },
    {
        "label": "01 定义",
        "title": "什么是 AI 产品设计",
        "subtitle": "核心不是“接了 AI”，而是“让用户更顺利地完成任务”。",
        "bullets": [
            "用户要解决什么问题",
            "AI 在哪一步真正帮上忙",
            "输出结果是否可用、可改、可继续操作",
        ],
        "footer": "判断标准：有没有形成真正可用的产品体验",
    },
    {
        "label": "02 区别",
        "title": "它和传统产品设计有什么不同",
        "subtitle": "传统产品偏确定流程，AI 产品更生成式，也更不稳定。",
        "bullets": [
            "输入可能不完整，需要引导澄清",
            "输出不一定唯一，需要支持修改和重试",
            "系统可能出错，需要兜底和反馈机制",
        ],
        "footer": "所以 AI 产品更重视输入引导、结果展示、错误处理",
    },
    {
        "label": "03 结构",
        "title": "记住这个最小工作流",
        "subtitle": "先用一个简单框架理解 AI 产品怎么运作。",
        "bullets": [
            "用户目标",
            "用户输入",
            "AI 处理",
            "结果输出",
            "用户修正 / 追问 / 继续操作",
        ],
        "footer": "这个闭环比“做个聊天框”更重要",
    },
    {
        "label": "04 价值",
        "title": "AI 产品通常靠什么创造价值",
        "subtitle": "先判断它是否真的比传统方式更有帮助。",
        "bullets": [
            "帮用户节省时间",
            "降低专业门槛",
            "提升内容质量",
            "提供灵感或备选方案",
        ],
        "footer": "不是所有问题都适合用 AI 做",
    },
    {
        "label": "05 误区",
        "title": "第一天先避开这 4 个坑",
        "subtitle": "少走弯路，比记一堆名词更重要。",
        "bullets": [
            "只关注模型强不强，不关注用户任务",
            "把产品做成万能聊天框，没有具体场景",
            "默认 AI 输出就是最终答案",
            "忽略 AI 会跑偏、会出错、会不稳定",
        ],
        "footer": "AI 产品设计一定要把不确定性纳入体验设计",
    },
    {
        "label": "06 练习",
        "title": "今天就做这两个小练习",
        "subtitle": "学完立刻动手，理解会更稳。",
        "bullets": [
            "拆 3 个 AI 产品：用户任务、AI 省掉哪一步、结果能否修改",
            "写 1 句话：AI 产品设计和传统产品设计最大的区别是什么",
            "整理 1 页笔记：定义、区别、结构、适用场景",
        ],
        "footer": "练习的目标：建立判断框架，而不是背概念",
    },
    {
        "label": "07 总结",
        "title": "一句话记住今天",
        "subtitle": "先判断用户问题，再判断 AI 为什么适合介入，最后思考体验如何承接不确定性。",
        "bullets": [
            "先看用户任务",
            "再看 AI 能力与边界",
            "最后看产品交互怎么落地",
        ],
        "footer": "下一步可以接着学：AI 能力与限制",
    },
]


def make_gradient():
    image = Image.new("RGB", (WIDTH, HEIGHT), BG_TOP)
    draw = ImageDraw.Draw(image)
    for y in range(HEIGHT):
        ratio = y / max(HEIGHT - 1, 1)
        color = tuple(
            int(BG_TOP[i] * (1 - ratio) + BG_BOTTOM[i] * ratio) for i in range(3)
        )
        draw.line((0, y, WIDTH, y), fill=color)
    return image


def load_font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_PATH, size=size)


def wrap_text(draw, text, font, max_width):
    words = list(text)
    lines = []
    current = ""
    for char in words:
        candidate = current + char
        if draw.textlength(candidate, font=font) <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = char
    if current:
        lines.append(current)
    return lines


def draw_wrapped(draw, text, font, x, y, width, fill, line_gap=10):
    lines = wrap_text(draw, text, font, width)
    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        y += font.size + line_gap
    return y


def rounded_rect(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def render_scene(index, scene):
    img = make_gradient()
    draw = ImageDraw.Draw(img)

    title_font = load_font(54)
    subtitle_font = load_font(26)
    label_font = load_font(22)
    bullet_font = load_font(34)
    footer_font = load_font(24)

    draw.ellipse((520, 70, 700, 250), fill=(255, 230, 222))
    draw.ellipse((40, 980, 190, 1130), fill=(255, 242, 205))

    rounded_rect(draw, (48, 64, 252, 114), 25, fill=(255, 255, 255), outline=(244, 221, 214), width=2)
    draw.text((72, 80), scene["label"], font=label_font, fill=ACCENT)

    y = 164
    y = draw_wrapped(draw, scene["title"], title_font, 56, y, 610, TEXT, line_gap=14)
    y += 24
    y = draw_wrapped(draw, scene["subtitle"], subtitle_font, 56, y, 610, MUTED, line_gap=12)

    card_top = y + 36
    card_bottom = HEIGHT - 170
    rounded_rect(draw, (40, card_top, WIDTH - 40, card_bottom), 36, fill=CARD, outline=CARD_BORDER, width=2)

    bullet_y = card_top + 46
    for bullet in scene["bullets"]:
        draw.ellipse((68, bullet_y + 14, 84, bullet_y + 30), fill=ACCENT)
        bullet_y = draw_wrapped(draw, bullet, bullet_font, 108, bullet_y, 540, TEXT, line_gap=12)
        bullet_y += 22

    draw.line((58, HEIGHT - 120, WIDTH - 58, HEIGHT - 120), fill=(238, 229, 215), width=2)
    draw_wrapped(draw, scene["footer"], footer_font, 58, HEIGHT - 98, 600, MUTED, line_gap=8)

    img.save(OUT / f"scene-{index:02d}.png")


def main():
    for i, scene in enumerate(SCENES, start=1):
        render_scene(i, scene)
    print(f"Rendered {len(SCENES)} slides to {OUT}")


if __name__ == "__main__":
    main()
