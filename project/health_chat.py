import pygame
import sys
import textwrap
import webbrowser 
import csv
from collections import Counter
import os


pygame.init()




screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("신체 부위 선택")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

try:
    font = pygame.font.SysFont("malgungothic", 28)

except:
    font = pygame.font.SysFont(None, 28)

body_img = pygame.image.load("project/body_imageimage.png")
body_img = pygame.transform.scale(body_img, (screen_width, screen_height))


body_parts = {
    "목(neck)": pygame.Rect(188, 173, 60, 50),
    "어깨_왼쪽": pygame.Rect(124, 188, 100, 50),
    "어깨_오른쪽": pygame.Rect(277, 188, 100, 50),
    "팔꿈치_왼쪽": pygame.Rect(99, 306, 60, 50),
    "팔꿈치_오른쪽": pygame.Rect(292, 304, 60, 50),
    "손목_왼쪽": pygame.Rect(86, 388, 60, 50),
    "손목_오른쪽": pygame.Rect(340, 388, 60, 50),
    "무릎_왼쪽": pygame.Rect(160, 509, 100, 80),
    "무릎_오른쪽": pygame.Rect(228, 509, 100, 80),
    "발목_왼쪽": pygame.Rect(172, 657, 60, 50),
    "발목_오른쪽": pygame.Rect(234, 657, 60, 50),
    "견갑": pygame.Rect(571, 210, 100, 100)
}

selected_answer = []
selected_part = None
options = []
option_rects = []
link_rect = pygame.Rect(150, 740, 500, 30)
link_text = "▶ 관련 설명을 유튜브에서 보기"
youtube_link = None 

def draw_options(part):
    global options
    if "목(neck)" in part:
        options = ["근육 기능 약화_목", "안 좋은 생활 습관_목", "운동 시 잘못된 자세_목"]
    elif "어깨" in part:
        options = ["근육 기능 약화_어깨", "안 좋은 생활 습관_어깨", "운동 시 잘못된 자세_어깨"]
    elif "팔꿈치" in part:
        options = ["근육 불균형_팔꿈치", "과한 운동_팔꿈치", "운동 시 잘못된 자세_팔꿈치"]
    elif "손목" in part:
        options = ["손목터널증후군", "운동 시 잘못된 자세_손목"]
    elif "무릎" in part:
        options = ["근육 불균형_무릎", "평소 걸음 문제", "운동 시 잘못된 자세_무릎"]
    elif "발목" in part:
        options = ["아킬레스건염", "염좌"]
    elif "견갑" in part:
        options = ["근육 기능 약화_견갑", "운동 시 잘못된 자세_견갑"]
    else:
        options = []

def draw_text_box(part, options):
    global option_rects
    option_rects.clear()

    title_text = f"{part} 부위에 통증이나 불편함이 있다면, 아래 항목을 의심해볼 수 있어요."
    wrapped_text = textwrap.wrap(title_text, width=20)

    box_width = 500
    box_height = 40 * len(wrapped_text) + len(options) * 50 + 40
    box_x = (screen_width - box_width) // 2
    box_y = 50

    pygame.draw.rect(screen, GRAY, (box_x, box_y, box_width, box_height), border_radius=10)
    pygame.draw.rect(screen, BLACK, (box_x, box_y, box_width, box_height), 2, border_radius=10)

    for i, line in enumerate(wrapped_text):
        text_surface = font.render(line, True, BLACK)
        screen.blit(text_surface, (box_x + 20, box_y + 15 + i * 35))

    for i, option in enumerate(options):
        opt_rect = pygame.Rect(box_x + 30, box_y + 40 + len(wrapped_text) * 35 + i * 50, box_width - 60, 40)
        pygame.draw.rect(screen, WHITE, opt_rect, border_radius=5)
        pygame.draw.rect(screen, BLACK, opt_rect, 1, border_radius=5)
        opt_text = font.render(f"{i+1}. {option}", True, BLACK)
        screen.blit(opt_text, (opt_rect.x + 10, opt_rect.y + 8))
        option_rects.append((opt_rect, option))

def draw_answer_box(answer):
    box_width = 500
    box_height = 200 * len(answer)
    box_x = (screen_width - box_width) // 2
    box_y = 50

    pygame.draw.rect(screen, GRAY, (box_x, box_y, box_width, box_height), border_radius=10)

    for i, line in enumerate(answer):
        text_surface = font.render(line, True, BLACK)
        screen.blit(text_surface, (box_x + 20, box_y + 15 + i * 35))

    if selected_answer and youtube_link:
        pygame.draw.rect(screen, (230, 230, 255), link_rect, border_radius=5)
        pygame.draw.rect(screen, BLACK, link_rect, 1, border_radius=5)
        link_surface = font.render(link_text, True, (0, 0, 255))
        screen.blit(link_surface, (link_rect.x + 10, link_rect.y + 5))


clock = pygame.time.Clock()


running = True
while running:
    screen.fill(WHITE)
    screen.blit(body_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:

            pos = pygame.mouse.get_pos()
            if link_rect.collidepoint(pos) and youtube_link:
                 webbrowser.open(youtube_link)
            
            print(pos)
            for part, rect in body_parts.items():
                if rect.collidepoint(pos):
                    selected_part = part
                    draw_options(part)
                    print(f"현재 선택된 부위: {part}")

                    csv_file = "log.csv"
                    if not os.path.exists(csv_file):
                        with open(csv_file, mode="w", newline="", encoding="utf-8-sig") as f:
                            writer = csv.writer(f)
                            writer.writerow(["part"])

                    with open(csv_file, mode="a", newline="", encoding="utf-8-sig") as f:
                        writer = csv.writer(f)
                        writer.writerow([part])

                    with open(csv_file, mode="r", encoding="utf-8-sig") as f:
                        reader = csv.reader(f)
                        next(reader) 
                        part_list = [row[0] for row in reader]
                    count_dict = Counter(part_list)

                    if count_dict[part] >= 5:
                        selected_answer = [
                            f"{part} 부위가 총 {count_dict[part]}회",
                            "선택되었습니다.",
                            "지속적인 통증이 의심되므로",
                            "전문가의 진료가 권장됩니다."
                        ]
                        youtube_link = None
                    
            for rect, option in option_rects:
                if rect.collidepoint(pos): 
                    selected_answer = []
                    print(f"선택된 옵션: {option}")
                    if option == "근육 기능 약화_목":
                        selected_answer = [
                                "승모근의 약화 혹은 목 주위 ",
                                "견갑거근의 단축성 긴장 등으로",
                                "체형이 하견체형처럼",
                                "어깨가 쳐지는 등의 문제가 발견되",
                                "었을 수 있습니다 승모근 운동이",
                                "필요해보입니다."
                                
                            ]
                        youtube_link = "https://www.youtube.com/shorts/A_KY3usZSeo"
                     
                    elif option == "안 좋은 생활 습관_목":
                        selected_answer = [
                            "장시간의 스마트폰 사용 혹은 컴퓨터",
                            "사용, 잘못된 공부 자세 등으로 인하여",
                            "목을 앞으로 내민 승모근의 기능을 ",
                            "약화시키고 견갑거근을 무리시켜 긴장",
                            "상태로 만들 가능성이 있습니다"
                        ]
                        youtube_link = "https://www.youtube.com/watch?v=zKJ7915100c"

                    elif option == "운동 시 잘못된 자세_목":
                        selected_answer = [
                            "슈러그를 만약에 이미 즐겨하고 있는",
                            "사람이라면 근육 기능 약화보다는",
                            "잘못된 자세가 문제일 가능성이",
                            "높습니다 슈러그를 할 때",
                            "이완시에 무리한 범위까지 이완하지",
                            "말고 수축을 좀 더 집중해주시고",
                            "견갑의 상방회전을 신경써서",
                            "이미 긴장되있는 견갑거근보다",
                            "승모근의 활성도를 높일 수 있도록",
                            "해주세요.",
                            "또한 로우 운동을 할때 본인도 모르게",
                            "몸을 뒤로 기울이고 머리를 앞으로",
                            "빼며 반동을 쓰는 안 좋은 운동 습관",
                            "운동 습관은 목에 데미지를",
                            "누적시킬 수 있습니다."
                        ]
                        youtube_link = "https://www.youtube.com/shorts/fJLqozfqT0A"

                    elif option == "근육 기능 약화_어깨":
                        selected_answer = [
                            "회전근개의 약화로 인한 문제와",
                            "어깨충돌로 인한 통증이 동반되고",
                            "있을 가능성이 높습니다.",
                            "이는 근본적으로 견갑 주변부 근육",
                            "들이 견갑의 기능을 약화시켜",
                            "어깨의 가동범위를 줄이거나 막아",
                            "다양한 결과가 유발되었을 수 있습니다.",
                            "견갑 주변부 근육의 활성화와 ",
                            "어깨 가동을 방해하는 소흉근,  ",
                            "대흉근의 긴장완화가 필요해보입니다."
                        ]
                        youtube_link = "https://www.youtube.com/watch?v=1maBEd3LpyU"

                    elif option == "안 좋은 생활 습관_어깨":
                        selected_answer = [
                            "컴퓨터나 스마트폰의 장시간 사용으로",
                            "목을 앞으로 내밀어서 거북목증후군,",
                            "어깨를 앞으로 계속 내밀고 있어서 ",
                            "라운드숄더 등을 갖고 계실 가능성이",
                            "높습니다. 견갑 주변부 근육들의 기능",
                            "들이 약화되고 소흉근, 견갑거근 등의",
                            "근육들은 긴장하고 단축되어 몸이 ",
                            "전체적으로 외회전 기능이 떨어져",
                            "있을 것 입니다. 몸의 앞쪽 근육들을",
                            "스트레칭 해주고 뒷쪽 근육들의 강화가",
                            "필요합니다."
                        ]
                        youtube_link = "https://www.youtube.com/shorts/19cHC_dJiM8"

                    elif option == "운동 시 잘못된 자세_어깨":
                        selected_answer = [
                            "어깨는 소켓 구조로 이루어져 자유로운",
                            "가동이 가능하지만 그만큼 불안정",
                            "한 관절입니다 다양한 문제가 있겠지만",
                            "먼저 체크할 점이 여러가지 있습니다",
                            "1. 어깨 운동 시작 전 가슴을 뒤집지",
                            "않고 완전한 만세가 가능한가요?",
                            "안된다면 견갑의 활성화와 소흉근 ",
                            "긴장 완화가 먼저입니다.",
                            "2. 프리웨이트에서 프레스류 운동 시에",
                            "전완과 땅이 수직이 맞나요?",
                            "아니라면 어깨 관절에 잘못된 방향으로",
                            "힘을 가하게 되어 무리를 줍니다. ",
                            "3. 견갑 활성화가 안된 상태에서는",
                            "고립보다는 몸의 협응에 집중해주세요."

                        ]
                        youtube_link = "https://www.youtube.com/watch?v=aae6UOmVeXM"

                    elif option == "근육 불균형_팔꿈치":
                        selected_answer = [
                            "모든 근육은 서로 앞뒤에 위치해있는",
                            "길항근끼리의 균형이 맞아야합니다.",
                            "이 경우에도 이두근과 삼두근의",
                            "발달이 서로 과도하게 차이가",
                            "나는 것이 의심이 됩니다."
                        ]
                        youtube_link = "https://www.youtube.com/watch?v=U5_a4PD51Ug"

                    elif option == "과한 운동_팔꿈치":
                        selected_answer = [
                            "모든 팔 운동은 어쩔 수 없이",
                            "관절과 인대를 사용합니다. ",
                            "팔 운동을 끝낸 뒤에는 꼭 근육뿐",
                            "아닌 인대와 신경의 회복 시간도 ",
                            "여유롭게 주어야 합니다.",
                            "팔을 키우고 싶다고 팔 운동의 ",
                            "빈도수를 너무 높이기 보다는",
                            "한번 운동할 때 강도를 올려주세요."

                        ]
                        youtube_link = "https://www.youtube.com/shorts/u-bgbCT1Tz8"

                    elif option == "운동 시 잘못된 자세_팔꿈치":
                        selected_answer = [
                            "다양한 의심가는 부분이 있지만",
                            "가장 먼저 의심가는 부분은 ",
                            "본인의 체형이 외반주인지 내반주인지",
                            "확인해보아야합니다. ",
                            "팔꿈치가 앞을 보게 팔을 자연스럽게",
                            "아래로 내렸을때 손이 과하게 바깥을",
                            "향했다면 외반주 반대라면",
                            "내반주입니다. 외반주 체형은 일자바로",
                            "바벨컬이 불가합니다. 손목을",
                            "내회전해서 운동할 수 있도록 이지바를",
                            "사용해주시고 프레스류 운동시에는 ",
                            "전완이 땅과 수직이 될 수 있게",
                            "신경써서 최대한 팔꿈치 인대와",
                            "관절의 부담을 덜어주세요."
                        ]
                        youtube_link = "https://www.youtube.com/watch?v=Rf_ak5eftCw"

                    elif option == "손목터널증후군":
                        selected_answer = [
                            "손목 신경이 압박되어 저림과",
                            "통증 발생이 가능하므로 평소 ",
                            "습관을 잘 체크하고 마우스, ",
                            "키보드 사용시에 손목이 땅과",
                            "수평인 상태를 계속 유지하기보다는",
                            "수직인 상태가 무리를 덜 줍니다. ",
                            "평소 의식적으로 손목을 수직으로 세워",
                            "작업하거나 버티컬 마우스를 사용하면",
                            "증상 완화에 도움이 될 수 있습니다."
                        ]
                        youtube_link = "https://www.youtube.com/watch?v=_dp2X55PePg"
                    
                    elif option == "운동 시 잘못된 자세_손목":
                        selected_answer = [
                            "프레스류 운동에서 손목 꺾임 발생이",
                            "가장 흔한 문제입니다. 프레스류",
                            "운동시에 오버그립보다는 프레스 그립",
                            "또는 썸리스 그립을 사용하여 손목의",
                            "부담을 줄여주세요."
                            
                        ]
                        youtube_link = "https://www.youtube.com/watch?v=Z8fG8WorU0E"

                    elif option == "근육 불균형_무릎":
                        selected_answer = [
                            "의외로 흔한 유형은 일단 길항근",
                            "즉 대퇴사두근과 대퇴이두의 ",
                            "불균형발달 문제입니다.",
                            "레그익스텐션과 레그컬을 진행",
                            "했을 때 다룰 수 있는 중량 차이가",
                            "운동을 균형있게 진행해 불균형을 ",
                            "고쳐주세요. ",
                            "혹은 대퇴사두근 중에서도 내전근이",
                            "발달 못하고 외측만 발달했을 때도",
                            "무릎의 안정성이 굉장히 떨어집니다.",
                            "내전근 운동을 하고 하체운동을 할때",
                            "고립보다는 협응에 좀 더",
                            "신경써주세요."
                        ]
                        youtube_link = "https://www.youtube.com/watch?v=6hZHt4Lv6is"

                    elif option == "평소 걸음 문제":
                        selected_answer = [
                            "평소 팔자걸음으로 걷는다던지 등의",
                            "걷는 습관이 문제가 될 수 있습니다.",
                            "재활의학과에 가서 골반축 정렬, 무릎",
                            "정렬이 맞는지 확인해보시고 문제가",
                            "크게 없다면 평소 둔근의 활성화가",
                            "안되어 걸을 때 고관절에서 ",
                            "충격 분배를 못해주고 무릎이 온전히",
                            "충격을 받고 있을 수 있습니다.",
                            "발을 내딛을때 둔근에 신경써주시고",
                            "발을 착지할때도 발바닥 전체로 밟을",
                            "수 있게 해주세요."
                        ]
                        youtube_link = "https://www.youtube.com/watch?v=fqtWd8c8AmM"

                    elif option == "운동 시 잘못된 자세_무릎":
                        selected_answer = [
                            "대부분 운동시에 대퇴직근의 활성화",
                            "를 걸지 못하고 무릎 근처에 부담",
                            "을 주는 것이 문제입니다.",
                            "처음부터 대퇴사두에만 고립을 ",
                            "걸려고 하기보다는 둔근 활성화",
                            "와 하체와 상체 협응에 집중하여",
                            "운동을 진행해주시고 스쿼트 시에는",
                            "무릎이 안쪽으로 과하게 붕괴되거나",
                            "고관절의 가동성이 부족하거나",
                            "발 중심을 잡지 못해 앞꿈치 혹은 ",
                            "뒷꿈치에만 무게 중심이 가는 등의",
                            "다양한 문제가 있어 스쿼트는 제대로",
                            "자세 교정 후 진행이 필요합니다."
                        ]
                        youtube_link = "https://www.youtube.com/watch?v=6hZHt4Lv6is"

                    elif option == "아킬레스건염":
                        selected_answer = [
                            "아킬레스건염에 걸리게 되면",
                            "아킬레스건이 먼저 부어오르며",
                            "건이 평소처럼 말랑하지않고",
                            "딱딱한 상태가 됩니다",
                            " 발 뒤꿈치의 과한 충격으로",
                            "인대가 긴장상태가 된 것이므로",
                            "아킬레스건을 쭉 늘려주는",
                            "스트레칭이 필요합니다."
                            "또한 평소에 발뒤꿈치로",
                            "착지하는 습관이 있다면",
                            "고쳐야 합니다."

                        ]
                        youtube_link = "https://www.youtube.com/watch?v=k8gausr6hEo"
                    
                    elif option == "염좌":
                        selected_answer = [
                            "갑작스런 뒤틀림으로 인한 인대 손상",
                            "입니다. 발목 바깥쪽에 통증이",
                            "주로 발생하며 심한 경우 붓기와",
                            "멍이 발생합니다 병원 진단과",
                            "휴식이 필요합니다."
                        ]
                        youtube_link = "https://www.youtube.com/shorts/yctk3SZF8pMQ"

                    elif option == "근육 기능 약화_견갑":
                        selected_answer = [
                            "상체 대부분의 부상의 원인",
                            "입니다 견갑이 제대로 기능을",
                            "해주지 못하면 어깨의 가동성",
                            "목의 가동성 등 다양한 문제가",
                            "발생하게 됩니다. ",
                            "상부, 중부, 하부 승모근의 ",
                            "활성화와 광배근의 긴장 완화",
                            "전거근의 강화와 소흉근 이완",
                            "등 다양한 운동과 스트레칭이",
                            "지속적으로 취해져야 견갑의",
                            "기능을 제대로 사용해 어깨충돌",
                            "목디스크, 익상견갑 등 다양한",
                            "문제를 고칠 수 있습니다."

                        ]
                        youtube_link = "https://www.youtube.com/watch?v=TmyqnEkfXvc"

                    elif option == "운동 시 잘못된 자세_견갑":
                        selected_answer = [
                            "운동 시 너무나도 다양한",
                            "부상 유발 자세가 있지만",
                            "몇 가지만 꼽자면 먼저",
                            "1. 벤치프레스 시 과도한 ",
                            "견갑 고정은 어깨에는 안전",
                            "할 수 있지만 목과 견갑에",
                            "데미지를 누적시켜 벤치에",
                            "누워서 고정시키더라도 미세한",
                            "견갑의 움직임은 사용할",
                            "수 있습니다.",
                            "2. 등 운동시 승모근을 견갑의",
                            "움직임을 배제시켜 견갑의 활성화",
                            "를 낮추게 되면 부상을 유발합니다.",
                            "견갑의 협응을 신경쓰고 가동범위를",
                            "가능한 많이 가져가야 합니다.",
                            "3.등 운동은 다양한 각도로 해줘야 할",
                            "필요가 있습니다 슈러그 혹은 풀오버,",
                            "다양한 동작을 진행해주세요."
                        ]
                        youtube_link = "https://www.youtube.com/watch?v=ffAUW0F45Y8"
    if selected_part:
        draw_text_box(selected_part, options)

    if selected_answer:
        draw_answer_box(selected_answer)

            

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()