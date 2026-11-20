# 미국 증시 데일리 아카이브

## 최초 설정 (1회)
1. github.com 가입 후 New repository → 이름 예: us-market → Public → Create
2. "uploading an existing file" 클릭 → 이 압축을 푼 폴더 안의 파일·폴더 전체를 끌어다 놓기 → Commit
   (.github 폴더가 안 올라가면 Add file → Create new file에서 이름을 .github/workflows/deploy.yml 로 하고 내용 붙여넣기)
3. Settings → Pages → Source를 "GitHub Actions"로 선택
4. Actions 탭에서 "Deploy site"가 초록색이 되면 https://<아이디>.github.io/us-market/ 로 접속

## 매일 추가
reports 폴더 → Add file → Upload files → us_market_YYYY-MM-DD.json 올리고 Commit.
(파일 이름은 YYYY-MM-DD.json 또는 us_market_YYYY-MM-DD.json 둘 다 가능)
1~2분 뒤 사이트에 자동 반영됩니다. 목록(manifest.json)은 자동으로 만들어집니다.
