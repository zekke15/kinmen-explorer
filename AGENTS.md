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
