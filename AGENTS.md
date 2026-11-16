# 金門慢遊｜AI 開發規則

## 目的
製作可持續新增景點的繁體中文金門介紹網站。開工先讀本檔、README.md、NOTES.md 和 content/places.json。

## 結構
- content/places.json：景點唯一資料來源。
- scripts/build.py：從資料與範本生成首頁卡片及 detail 頁面。
- templates/index.html、templates/detail.html：頁面範本。
- dist/：可以直接發布的網站，包括 index.html、places/、assets/。
- dist/assets/style.css：全站共用樣式；app.js：搜尋與分類互動。
- dist/assets/*.svg：原創線條插畫，為意象而非實景照片。
- .openai/hosting.json：預覽平台設定；不要改動 project_id。

## 內容規則
每筆景點包含 id、name、english、category、town、summary、intro、highlights（三項）、tips、source、art。
id 使用小寫英文與連字號且不得重複。分類限定聚落建築、戰地歷史、自然風景、街區漫步。
簡介不超過 55 個中文字。詳細頁固定包含景點介紹、三個觀察重點、到訪提醒及官方資料來源。
官方來源優先使用金門觀光旅遊網，先查證再寫。不編造開放時間、票價、歷史年份、即時交通或評分。需即時資訊時引導至官方公告。

## 視覺與互動
淺灰背景 #f4f7f8、深藍文字 #17313a、青綠重點 #087f76；使用系統字體。首頁雙欄、卡片三欄，760px 以下單欄。圓角、留白、細線邊框延續全站。
分類按鈕與搜尋必須同時生效；顯示結果數、無結果訊息、清除按鈕。分類狀態用 aria-pressed。卡片保留真實 href，即使 JavaScript 關閉仍可看景點。
使用相對路徑支援 GitHub Pages 子路徑與離線開啟。所有動態文字以 textContent 寫入。按鈕最小 44px、有可見鍵盤焦點、避免水平溢出。

## 新增流程
1. 查閱官方資料，新增 content/places.json 的完整物件。
2. 沿用既有 art 或新增原創 SVG；不可把示意插畫描述成實拍。
3. 執行 python scripts/build.py，產生首頁與詳細頁。不要只改生成的 HTML。
4. 執行 python scripts/check.py，檢查資料欄位、唯一 id、本機連結及輸出。
5. 在瀏覽器驗證分類、中文搜尋、英文搜尋、組合篩選、零結果、清除、景點進出與鍵盤焦點。
6. 更新 NOTES.md、CHANGELOG.md；回報真實測試結果及限制。

## 維護
不移除無關頁面、不複製既有網站品牌素材、不加入第三方追蹤與金鑰。更動共用 CSS 後檢查首頁和詳細頁。規則變更同步記錄原因；任何未做的驗證明確寫未驗證。

## 執行與發布
python scripts/build.py；python scripts/check.py。
本機可直接開 dist/index.html，或 python -m http.server 8000 --directory dist。
GitHub Pages 發布：將 dist 裡的內容放到新倉庫根目錄，開啟 main / (root)；同時上傳本規則、content、scripts、templates 與 README 供後續維護。請勿聲稱未建立的 GitHub 網址已可用。

## 景點欄位對照

所有欄位均必填。除 highlights 為字串陣列外，其餘欄位都是字串。

| 欄位 | 用途與限制 |
| --- | --- |
| id | 唯一英文代號，例如 shuitou-village；會成為詳細頁檔名 |
| name | 繁體中文景點名稱 |
| english | 英文名稱，供卡片顯示與搜尋 |
| category | 既定四類之一；新增分類時需同步修改產生器、檢查程式與首頁範本的分類數 |
| town | 景點所在鄉鎮，不猜測行政區 |
| summary | 55 個字元以內的卡片簡介，以現有檢查程式的 len 計算為準 |
| intro | 經查證後自行撰寫的景點介紹，不直接抄錄完整原文 |
| highlights | 恰好三項可觀察的特色，不使用無依據的排名或評分 |
| tips | 參觀提醒；不將未查證的即時資訊寫成確定事實 |
| source | 官方來源完整 HTTPS 網址；現有檢查要求 https://kinmen.travel/ 開頭 |
| art | 插畫檔名，不含 .svg；對應 dist/assets/<art>.svg |

目前可沿用的 art：tower、village、tunnel、lake、street。若沿用意象插畫，替代文字與說明仍須標明是示意。

## 哪裡應該修改

| 任務 | 修改位置 | 後續動作 |
| --- | --- | --- |
| 修改景點文字或新增景點 | content/places.json | 重新產生並檢查網站 |
| 修改首頁結構 | templates/index.html | 重新產生首頁 |
| 修改所有景點頁結構 | templates/detail.html | 重新產生全部介紹頁 |
| 修改顏色、字體、間距與版面 | dist/assets/style.css | 檢查首頁及介紹頁 |
| 修改搜尋與分類 | dist/assets/app.js | 驗證組合篩選與空結果 |
| 修改卡片結構或生成規則 | scripts/build.py | 重新產生全部頁面並檢查 |

內容與範本是 HTML 的來源；不要只改 dist/index.html 或 dist/places/*.html，否則下次生成會被覆蓋。
目前產生器不會清除已刪除景點的舊 HTML。若使用者要求移除景點，應檢查其對應頁面與連結，僅移除該景點的過時產物，不清空整個 dist。

## 完成定義

- 新景點出現在首頁，點擊可開啟自己的介紹頁。
- 中文名稱、英文名稱、鄉鎮可搜尋到該景點。
- 分類與搜尋採交集：必須同時符合選定分類及關鍵字。
- 「清除篩選」清空關鍵字並恢復全部景點；結果數與可見卡片一致。
- 不符合任何景點時顯示明確提示，不留下空白畫面。
- 介紹頁包含景點介紹、三項特色、提醒、官方來源與返回連結。
- Python 產生與檢查命令成功；未執行的檢查不得宣稱通過。
- 桌面與手機版面需分別檢查；尚未測試手機時明確記錄限制。
- README 的功能清單、NOTES 的現況及 CHANGELOG 的變更與實作一致。

## 交接與回報

完成工作時列出：修改的檔案、使用的資料來源、實際執行的檢查、未完成項目。NOTES.md 記目前狀態與下一步；CHANGELOG.md 記已完成的變更與原因，不虛構歷史工作紀錄。

上傳 GitHub 時將本檔命名為 AGENTS.md，放在與 README.md、content、scripts、templates 同層的專案根目錄。網站使用者不需要 AI 工具也能正常瀏覽；這份文件是提供給開發者與 AI 的規則，不是網站執行所需的程式。

## 可直接交給 AI 的延伸指令

> 請先閱讀 AGENTS.md、README.md、NOTES.md 與 content/places.json。依照現有規則新增一個尚未收錄的金門景點：先查證官方資料，補齊所有欄位，沿用合適的意象插畫或新增原創 SVG，重新生成首頁與介紹頁，驗證分類、搜尋、返回連結及空結果處理，最後更新 NOTES.md、CHANGELOG.md 並回報實際檢查結果。
