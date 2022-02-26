# nonsan-trainee-news
![test workflow](https://github.com/guzus/nonsan-trainee-news/actions/workflows/test.yml/badge.svg)

Using [this](https://github.com/lewisleedev/thecampy) library for sending daily news to trainees.

## Flow

```mermaid
flowchart LR
A[A가 훈련소에 감] -->|부탁| B(B가 PR을 통해 README.md에 훈련생 정보를 추가함)
B --> C{Github Action}
C -->|성공| D[A에게 매일 따끈한 뉴스가 발송됨]
C -->|실패| E[A는 뉴스를 볼 수 없음]
```

## 훈련생 목록
매일 12시에 아래 표의 훈련생들에게 뉴스가 인터넷 편지 형태로 발송됩니다.
인터넷 편지를 발송할 훈련생의 정보를 추가하고 PR을 올려주세요.
| 이름  | 생일(yyyymmdd) | 입대일(yyyymmdd) | 부대명(ex: 육군훈련소) | groupName | unitName
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 정명구  | 20010301  | 20220310  | 육군훈련소  | Content Cell  | Content Cell  |
| Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell  |

## 제공되는 뉴스 목록
- [Hackernews Headline](https://news.ycombinator.com/newest)
- [연합뉴스 Headline](https://www.yonhapnewstv.co.kr/news/headline)
