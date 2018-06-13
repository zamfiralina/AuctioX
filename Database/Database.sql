DROP TABLE SITE_USERS CASCADE CONSTRAINTS ;
DROP TABLE ITEMS      CASCADE CONSTRAINTS ;
DROP TABLE AUCTIONS   CASCADE CONSTRAINTS ;
DROP TABLE CATEGORIES CASCADE CONSTRAINTS ;
DROP TABLE TAGS       CASCADE CONSTRAINTS ;


CREATE TABLE SITE_USERS ( USER_ID    NUMBER ,
                          FIRST_NAME VARCHAR2(50) NOT NULL ,
                          LAST_NAME  VARCHAR2(50)NOT NULL ,
                          EMAIL      VARCHAR2(100) NOT NULL ,
                          USERNAME   VARCHAR2(50) UNIQUE NOT NULL ,
                          PASSWORD   VARCHAR2(500) NOT NULL ,
                          COUNTRY    VARCHAR2(100) NOT NULL ,
                          CITY       VARCHAR2(100) NOT NULL ,
                          TELEPHONE  VARCHAR2(100) NOT NULL ,
                          LINK_PIC   VARCHAR2(200) NOT NULL ,

                          CONSTRAINT site_users_pk PRIMARY KEY (USER_ID),
                          CONSTRAINT valid_email   CHECK (EMAIL LIKE '%@%.%'));
                     

CREATE TABLE CATEGORIES (CATEGORY_ID   NUMBER ,
                         CATEGORY_NAME VARCHAR2(50) NOT NULL ,

                         CONSTRAINT categories_pk PRIMARY KEY (CATEGORY_ID));


CREATE TABLE ITEMS (ITEM_ID     NUMBER NOT NULL ,
                    USER_ID     NUMBER NOT NULL ,
                    P_NAME      VARCHAR2(100) NOT NULL ,
                    CATEGORY_ID NUMBER NOT NULL ,
                    PICTURE     VARCHAR2(1000) NOT NULL ,
                    S_PRICE     NUMBER NOT NULL ,
                    S_DATE      TIMESTAMP(6) NOT NULL ,
                    END_DATE    TIMESTAMP(6) NOT NULL ,
                    DESCRIPTION VARCHAR2(3000) ,

                    CONSTRAINT items_pk          PRIMARY KEY (ITEM_ID),
                    CONSTRAINT items_users_fk    FOREIGN KEY (USER_ID)     REFERENCES SITE_USERS(USER_ID),
                    CONSTRAINT items_category_fk FOREIGN KEY (CATEGORY_ID) REFERENCES CATEGORIES(CATEGORY_ID));


CREATE TABLE TAGS (ID                   NUMBER ,
                   ITEM_ID              NUMBER NOT NULL ,
                   CHARACTERISTIC_NAME  VARCHAR2(50),
                   CHARACTERISTIC_VALUE VARCHAR2(50),

                   CONSTRAINT item_category_pk    PRIMARY KEY (ID),
                   CONSTRAINT constraint_to_items FOREIGN KEY (ITEM_ID) REFERENCES ITEMS(ITEM_ID));


CREATE TABLE AUCTIONS (USER_ID NUMBER NOT NULL ,
                       ITEM_ID NUMBER NOT NULL ,
                       PRICE   NUMBER ,
                       
                       CONSTRAINT constraint_to_auction_items FOREIGN KEY (ITEM_ID) REFERENCES ITEMS(ITEM_ID),
                       CONSTRAINT constraint_to_auction_user  FOREIGN KEY (USER_ID) REFERENCES SITE_USERS(USER_ID));


insert into site_users values(1,'Nume','Prenume','email@gmail.com','username','pass','Romania', 'Iasi', '0232245456', 'https://www.bluecross.org.uk/sites/default/files/assets/images/124044lpr.jpg');
insert into site_users values(2,'Anca','Moisa','anca@gmail.com','ancam','parola1', 'Germania', 'Berlin', '0893294234', 'http://www.keresztenyelet.hu/wp-content/uploads/2018/03/Igazi-%C3%A1llatbar%C3%A1t.jpg');
insert into site_users values(3,'Alina','Zamfir','alina@gmail.com','alinaz','hr327g', 'Austria', 'Viena', '8364762398', 'https://www.moje-kocka.cz/foto-clanky/lkal2.jpg');
insert into site_users values(4,'Iulian','Andronache','iulian@gmail.com','aiuian','p32ruih', 'Romania', 'Brasov' , '073436277', 'https://d2kwjcq8j5htsz.cloudfront.net/2016/07/12163020/cat-elizabethan-collar-cone-TS-523822772-3.jpg');
insert into site_users values(5,'Flori','Tanasiu','tanasiu@gmail.com','florentina','387yhu', 'Romania', 'Dorohoi', '0745262353', 'http://i0.kym-cdn.com/entries/icons/original/000/002/232/bullet_cat.jpg');
insert into site_users values(6,'Rares','Dima','rdima@gmail.com','rdima','387yhu', 'Romania', 'Buzau', '072343645', 'http://r.ddmcdn.com/s_f/o_1/cx_0/cy_157/cw_1327/ch_1327/w_720/APL/uploads/2013/01/smart-cat-article.jpg');
insert into site_users values(7,'Matei','Tarevici','mtarevici@gmail.com','mtarevici','yhuuu', 'Romania', 'Suceava', '07482765842', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRWB6W7GLsVLLDYp72NtIGnB4r1aJVpVnOed17IB2abKLY_8tAl');
insert into site_users values(8,'Vasile','Popescu','vasi@gmail.com','vasipop','vasip', 'Franta', 'Paris', '015423542', 'https://cdn.shopify.com/s/files/1/0344/6469/products/New-Cute-Pet-Cat-Costume-Cartoon-Funny-Pet-Cat-Clothes-Hot-Puppy-Clothing-Doctor-Uniform-Hat_copy_1024x1024.jpg?v=1504800100');
insert into site_users values(9,'Ion','Ionescu','ionescu@gmail.com','ionion','387ion', 'Romania', 'Radauti', '072543372', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTbviSJcx2a4U01BRinV9aTIrdxUBzy9ZCHs2WdNG49aanJilZG');
insert into site_users values(10,'Alex','Alexa','alex@gmail.com','alex','alehu', 'Romania', 'Vaslui', '0231255255', 'https://ichef.bbci.co.uk/images/ic/720x405/p0517py6.jpg');

insert into categories values(1,'Animals');
insert into categories values(2,'Chloting, Shoes & Accessories');
insert into categories values(3,'Toys & Hobbies');
insert into categories values(4,'Motorcycles');
insert into categories values(5,'Home & Office');
insert into categories values(6,'Health & Beauty');
insert into categories values(7,'Electrical & Tools');
insert into categories values(8,'Consumer Electronics');

insert into items values(1,2,'sticla',6,'http://elelur.com/data_images/mammals/wolf/wolf-01.jpg',20,sysdate,sysdate,'sticla plastic suc piersici');
insert into items values(2,4,'cutit',7,'http://elelur.com/data_images/mammals/wolf/wolf-01.jpg',3000,sysdate,sysdate,'cutit spania ascutit');
insert into items values(3,2,'telefon',8,'http://elelur.com/data_images/mammals/wolf/wolf-01.jpg',500,sysdate,sysdate,'huawei p9 lite');
insert into items values(4,1,'laptop',8,'http://elelur.com/data_images/mammals/wolf/wolf-01.jpg',1000,sysdate,sysdate,'laptop negru prafuit');
insert into items values(5,1,'scaun',5,'http://elelur.com/data_images/mammals/wolf/wolf-01.jpg',300,sysdate,sysdate,'scaun verde scartaie');
insert into items values(6,10,'cafea',6,'http://elelur.com/data_images/mammals/wolf/wolf-01.jpg',10,sysdate,sysdate,'cafea da energie ca sa nu mori');
insert into items values(7,9,'geanta',2,'http://elelur.com/data_images/mammals/wolf/wolf-01.jpg',250,sysdate,sysdate,'geanta cara chestii something');
insert into items values(8,8,'incarcator',8,'http://elelur.com/data_images/mammals/wolf/wolf-01.jpg',180,sysdate,sysdate,'something something');
insert into items values(9,7,'papuci',2,'http://elelur.com/data_images/mammals/wolf/wolf-01.jpg',80,sysdate,sysdate,'talpa verde');
insert into items values(11,7,'pisica',1,'http://elelur.com/data_images/mammals/wolf/wolf-01.jpg',300,sysdate,sysdate,'cuminte si blanda');
insert into items values(12,7,'lup',1,'http://elelur.com/data_images/mammals/wolf/wolf-01.jpg',10000,sysdate,sysdate,'excelent animal de companie');
insert into items values(13,7,'caiet',5,'http://elelur.com/data_images/mammals/wolf/wolf-01.jpg',3,sysdate,sysdate,'numai bun de notite');
insert into items values(14,7,'motocicleta',4,'http://elelur.com/data_images/mammals/wolf/wolf-01.jpg',600,sysdate,sysdate,'brrrummm brrrumm');

insert into tags values(14,4,'color','rosie');
insert into tags values(15,4,'fabrication_year','1900');
insert into tags values(11,1,'other_spec','birmaneza');
insert into tags values(5,5,'color','verde');

insert into auctions values(4,12,123);
insert into auctions values(5,10,500);
insert into auctions values(3,13,200);
insert into auctions values(7,1,280);
insert into auctions values(7,7,800);
insert into auctions values(9,2,200);
insert into auctions values(9,3,200);
insert into auctions values(10,4,200);
insert into auctions values(1,5,200);
insert into auctions values(2,6,200);

COMMIT ;
