# Sweep Mac/Windows 전환

사용자가 승인한 Mac/Windows 런타임 전환 구조입니다. 실제 키보드에서 OS별 단축키를 확인하세요.

## 조작

- 기본은 Mac 모드로 부팅합니다.
- 왼손 안쪽 엄지 `Tab`을 길게 눌러 SYS 진입 → 물리 `W`를 한 번 누름 → 엄지 떼기.
- MAC SYS의 W: Windows 기본 레이어로 이동.
- WIN SYS의 W: Mac 기본 레이어로 이동.
- 같은 위치의 키 하나를 양방향으로 사용합니다. SYS 진입은 기존 그대로입니다.
- 전환 직후 SYS를 해제하고 선택한 OS의 기본 레이어로 돌아갑니다.
- 동글 OLED의 레이어 이름도 `MAC DEF`, `WIN DEF` 등으로 구분됩니다. OLED 자체 하드웨어 문제를 해결하는 변경은 아닙니다.
- 선택 상태는 전원 차단 후 저장하지 않습니다. 동글을 재부팅하면 Mac 모드로 시작합니다.

## 키 배열

모든 레이어는 기존 34키(10+10+10+4)입니다. 유일한 새 물리 바인딩은 SYS/W입니다.

```text
기본 위치
Q      W       E       R       T    | Y       U       I        O         P
A/GUI  S/Alt   D/Shift F/Ctrl  G    | H       J/Ctrl  K/Shift  L/Alt     '/GUI
Z      X       C       V       B    | N       M       ,/Shift  ./언어전환 /
                  Space/NAV Tab/SYS | Enter/SYM Backspace/NUM

SYS 위치 (— = 입력 없음, ▽ = 기본 레이어 동작)
Reset  OS전환   —       잠금    종료  | 종료    KP7     KP8      KP9       Reset
GUI    Alt      Shift   Ctrl    —    | —       KP4     KP5      KP6       —
BT전체초기화 BT0 BT1     BT2     BT삭제 | —       KP1     KP2      KP3       —
                        ▽      ▽    | —       KP0
```

GUI는 Mac에서 Command, Windows에서 Windows 키입니다. Alt는 Mac에서 Option입니다.
SYS의 `Reset`은 기존처럼 짧게 누르면 시스템 재시작, 길게 누르면 부트로더입니다.
`종료`는 Mac/PC 종료가 아니라 키보드 장치 soft-off입니다.

## 두 모드의 차이

| 기능 | Mac | Windows |
|---|---|---|
| 복사 / 붙여넣기 / 잘라내기 | Cmd+C / V / X | Ctrl+C / V / X |
| 실행 취소 / 다시 실행 | Cmd+Z / Cmd+Shift+Z | Ctrl+Z / Ctrl+Y |
| 전체 선택 콤보 | Cmd+A | Ctrl+A |
| 앱 전환 | Cmd+Tab | Alt+Tab |
| 탭 전환 | Ctrl+Tab | Ctrl+Tab |
| NAV 닫기 키: 탭 | Cmd+W | Ctrl+F4 |
| NAV 닫기 키: 홀드 | Cmd+Q (앱 종료) | Alt+F4 |
| 단어 앞/뒤 삭제 | Option+Backspace / Delete | Ctrl+Backspace / Delete |
| NAV 한 글자 앞으로 삭제 | Ctrl+D (기존 Mac 설정) | Delete |
| 줄 시작 / 끝 | Cmd+← / → | Home / End |
| 문서 시작 / 끝 | Cmd+↑ / ↓ | Ctrl+Home / End |
| 화면 잠금 | Ctrl+Cmd+Q | Win+L |
| 기본 `.` 홀드 | Ctrl+Option+Space | Right Alt (원본 Windows 설정 유지) |

Windows의 Right Alt 동작은 Windows 입력기 설정에 따르며, 네 언어 순환을 보장하는 매핑은 아닙니다.
Mac의 네 언어 전환용 Ctrl+Option+Space는 그대로 유지합니다.
숫자·기호·F키·마우스·미디어·Bluetooth·홈로우 Modifier 위치는 기존과 같습니다.

## 내부 구조

```text
0 MAC DEF    1 MAC NUM    2 MAC SYM    3 MAC NAV    4 MAC SYS
5 WIN DEF    6 WIN NUM    7 WIN SYM    8 WIN NAV    9 WIN SYS

MAC SYS/W → &to 5
WIN SYS/W → &to 0
```

사용자가 익힌 5레이어 조작 체계는 유지하고, 내부에서 OS별 5레이어를 각각 둡니다.
기존 NUM/NAV/SYS Shift+홀드 고정과 F+J 복귀 콤보도 양쪽 OS별로 작동합니다.
Windows 레이어의 투명 키는 Windows 기본 바인딩을 명시해, Shift+레이어 고정으로
WIN DEF가 비활성화되어도 Mac 레이어로 새지 않도록 했습니다.
콤보는 각 프로필의 해당 레이어에서만 활성화됩니다.

## 수정 파일 및 검증

- `config/sweep.keymap`: 런타임 전환 키맵 로드.
- `config/includes/sweep-dual-os.dtsi`: 10개 레이어, Windows 전용 레이어 홀드 동작, Windows 콤보.
- `scripts/generate_sweep_dual_os.py`: 기존 공용 3x5/shortcut/combos/behaviors 파일에서 전환 키맵 생성.
- `scripts/check_sweep_dual_os.py`: 실제 C 전처리로 10×34 바인딩, OS 전환, 엄지 라우팅, 콤보,
  Shift 고정 시 Windows 유지, 사용자 동작 label 중복 검사.

공용 키맵/동작 정의를 수정할 때는 다음을 실행해야 합니다.

```sh
python3 scripts/generate_sweep_dual_os.py
python3 scripts/check_sweep_dual_os.py
```

검사에서 외부 SDK 헤더만 대체합니다. Zephyr/ZMK 전체 컴파일이나 하드웨어 입력 검증을 대신하지 않습니다.
원래 공용 키맵을 사용하는 Totem에는 이 전환 기능을 적용하지 않습니다.

## 빌드 및 적용

1. 변경을 commit/push합니다.
2. GitHub Actions의 새 ZMK 컴파일 결과를 확인하고 오류가 있으면 수정합니다.
3. 성공한 새 `sweep_dongle.uf2`를 동글에 플래시합니다. 기존 페어링 초기화는 불필요합니다.
4. Studio에서 저장한 키맵이 있다면 백업한 다음 Restore Stock Settings로 새 10레이어 구조를 적용합니다.
   이 작업은 Studio에서 저장한 키맵 수정을 되돌립니다.
