INSERT INTO `news` (
    `title`,
    `source`,
    `create_date`,
    `description`,
    `look`
) VALUES (
    '新冠疫情來襲再掀企業線上學習熱潮', 
    '工商時報', 
    '2020-02-26', 
    '緯育TibaMe長期致力於企業培訓服務，聚焦在領導力、人工智慧、雲端應用、行動技術、數位商務、區塊鏈及科技管理等領域的數位力發展，提供多達 ...', 
    '100'
)

UPDATE `news` SET `look`= '999';
UPDATE `news` SET `look`= '100' WHERE `id` = 3;
UPDATE `news` SET `look`= '555' WHERE `id` <> 3;
UPDATE `news` SET `look`= '777' WHERE `id` in (3, 4, 5);
UPDATE `news` SET `look`= '222' WHERE `id` NOT IN (3, 4, 5);
UPDATE `news` SET `look`= '10' WHERE `description` LIKE '%AI%';
UPDATE `news` SET `look`= '0' WHERE `create_date` BETWEEN '2019-01-01' AND '2020-03-31';

UPDATE `news` SET `look`= '777' WHERE `id` = 3 OR `id` = 4;
UPDATE `news` SET `look`= '111' WHERE `id` = 3 AND `create_date` BETWEEN '2018-01-01' AND '2020-03-31';

--# 多項目設值
UPDATE `news` SET `look`= '999', `title` = '改標題';

--# 刪除, 刪除 id (主鍵)之後，日後不會重複號碼
DELETE FROM `news`;
DELETE FROM `news` WHERE `id` = 3;

SELECT `title`, `source` FROM `news` WHERE `id` > '1';
SELECT * FROM `news` WHERE `id` > '1';

SELECT * FROM `news` where `id` > '1' ORDER BY `look` ASC;
SELECT * FROM `news` WHERE `id` > '1' ORDER BY `look` DESC, `id` DESC;

--# id 大於 1，統計 id 個數
SELECT COUNT(`id`) FROM `news` WHERE `id` > '1';
--# id 大於 1, 計算加總 look 資料
SELECT SUM(`look`) FROM `news` WHERE `id` > '1';
--# id 大於 1, 計算平均 look 資料
SELECT AVG(`look`) FROM `news` WHERE `id` > '1';
--# AS 做別名
SELECT AVG(`look`) AS `AVG_look` FROM `news` WHERE `id` > '1';

--# 從第 1 筆 顯示兩筆資料 (顯示第二、三筆)
SELECT * FROM `news` LIMIT 1, 2;
SELECT * FROM `news` LIMIT 0, 2;
--# 從第 0 筆 顯示兩筆資料，顯示所有欄位，對 id 由大到小排序
SELECT * FROM `news` ORDER BY `id` DESC LIMIT 0, 2;



--# 以下使用 python_ai 資料庫 做操作

--# 資料表做關聯
SELECT * FROM `member` 
INNER JOIN `tel` 
ON `member`.`id` = `tel`.`member_id`;

-- 顯示兩個資料表做關聯所對應到的資料
SELECT `A`.`id`, `A`.`name`, `B`.`tel`
FROM `member` AS `A`
INNER JOIN `tel` AS `B` 
ON `A`.`id` = `B`.`member_id`;

--# 顯示關聯左邊資料表，顯示左邊所有資料表的資料
SELECT `A`.`id`, `A`.`name`, `B`.`tel`
FROM `member` AS `A`
LEFT JOIN `tel` AS `B` 
ON `A`.`id` = `B`.`member_id`;
-- 改變語法格式，利用 RIGHT 顯示
SELECT `A`.`id`, `A`.`name`, `B`.`tel`
FROM `tel` AS `A`
RIGHT JOIN `member` AS `B`
ON `A`.`id` = `B`.`member_id`;

--# 顯示關聯右邊資料表
SELECT `A`.`id`, `A`.`name`, `B`.`tel`
FROM `member` AS `A`
RIGHT JOIN `tel` AS `B` 
ON `A`.`id` = `B`.`member_id`;

SELECT `A`.`id`, `A`.`name`, `B`.`tel`
FROM `tel` AS `A`
LEFT JOIN `member` AS `B`
ON `A`.`id` = `B`.`member_id`;

-- 如果想確保關聯資料的一致性，可以使用外來鍵功能。 (開啟資料庫控制台設定 >>> 結構 >>> 關聯檢視 >>> 設定資料並儲存
--


--# 以下用 2020-03-31 資料庫
--# SQL 直接運算
SELECT `id`, `look` + 1000 FROM `news`;

UPDATE `news` SET `look` = `look` + 10;

SELECT * FROM `news` WHERE CONCAT(`title`, `description`) LIKE '%AI%';

INSERT INTO `news` (
    `title`,
    `source`,
    `create_date`,
    `description`,
    `look`
) VALUES (
    'xxx', 
    'bbb', 
    '2020-02-26', 
    'ddd', 
    100 * 2
)

SELECT * FROM `news` WHERE `look` = 0 + 10;


INSERT INTO `tel` (
    `member_id`, 
    `tel`
) VALUES (
    '3',
    '5555-6666'
);