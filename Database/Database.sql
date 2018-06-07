DROP TABLE SITE_USERS     CASCADE CONSTRAINTS ;
DROP TABLE ITEMS     CASCADE CONSTRAINTS ;
DROP TABLE AUCTIONS    CASCADE CONSTRAINTS ;
DROP TABLE CATEGORIES     CASCADE CONSTRAINTS ;
DROP TABLE ITEM_CATEGORY    CASCADE CONSTRAINTS ;


CREATE TABLE SITE_USERS ( USER_ID NUMBER ,
                          FIRST_NAME VARCHAR2(30) NOT NULL ,
                          LAST_NAME VARCHAR2(50)NOT NULL ,
                          EMAIL VARCHAR2(100) NOT NULL ,
                          USERNAME VARCHAR2(50) UNIQUE NOT NULL ,
                          PASSWORD VARCHAR2(50) NOT NULL ,

                          CONSTRAINT site_users_pk PRIMARY KEY (USER_ID),
                          CONSTRAINT valid_email CHECK (EMAIL LIKE '%@%.%'));
                     
                     
                     
                     
CREATE TABLE ITEMS (ITEM_ID NUMBER ,
                    USER_ID NUMBER ,
                    TITLE VARCHAR2(100) NOT NULL ,
                    DESCRIPTION VARCHAR2(3000) NOT NULL ,
                    START_DATE TIMESTAMP(6) NOT NULL ,
                    END_DATE TIMESTAMP(6) NOT NULL ,
                    
                    CONSTRAINT items_pk PRIMARY KEY (ITEM_ID),
                    CONSTRAINT items_users_fk FOREIGN KEY (USER_ID) REFERENCES SITE_USERS(USER_ID));
                    
                    
                    
                    
CREATE TABLE CATEGORIES (CATEGORY_ID NUMBER ,
                         CATEGORY_NAME VARCHAR2(50) NOT NULL ,

                        CONSTRAINT categories_pk PRIMARY KEY (CATEGORY_ID));
                         
                         
                         
CREATE TABLE ITEM_CATEGORY (ID NUMBER ,
                            ITEM_ID NUMBER NOT NULL ,
                            CATEGORY_ID NUMBER NOT NULL ,

                            CONSTRAINT item_category_pk       PRIMARY KEY (ID),
                            CONSTRAINT constraint_to_items      FOREIGN KEY (ITEM_ID)     REFERENCES ITEMS(ITEM_ID),
                            CONSTRAINT constraint_to_categories FOREIGN KEY (CATEGORY_ID) REFERENCES CATEGORIES(CATEGORY_ID));


                            
                            
                            
                            
CREATE TABLE AUCTIONS (USER_ID NUMBER NOT NULL ,
                       ITEM_ID NUMBER NOT NULL ,
                       PRICE NUMBER ,
                       
                       CONSTRAINT constraint_to_auction_items      FOREIGN KEY (ITEM_ID)     REFERENCES ITEMS(ITEM_ID),
                       CONSTRAINT constraint_to_auction_user      FOREIGN KEY (USER_ID)     REFERENCES SITE_USERS(USER_ID));
                       
                       
                       

                       

insert into site_users values(1,'Nume','Prenume','email@gmail.com','username','pass');
insert into site_users values(2,'Anca','Moisa','anca@gmail.com','ancam','parola1');
insert into site_users values(3,'Alina','Zamfir','alina@gmail.com','alinaz','hr327g');
insert into site_users values(4,'Iulian','Andronache','iulian@gmail.com','aiuian','p32ruih');
insert into site_users values(5,'Flori','Tanasiu','tanasiu@gmail.com','florentina','387yhu');
insert into site_users values(6,'Rares','Dima','rdima@gmail.com','rdima','387yhu');
insert into site_users values(7,'Matei','Tarevici','mtarevici@gmail.com','mtarevici','yhuuu');
insert into site_users values(8,'Vasile','Popescu','vasi@gmail.com','vasipop','vasip');
insert into site_users values(9,'Ion','Ionescu','ionescu@gmail.com','ionion','387ion');
insert into site_users values(10,'Alex','Alexa','alex@gmail.com','alex','alehu');

insert into items values(12,2,'sticla','sticla plastic suc piersici',sysdate,sysdate);
insert into items values(13,4,'cutit','cutit spania ascutit',sysdate,sysdate);
insert into items values(10,2,'telefon','huawei p9 lite',sysdate,sysdate);
insert into items values(5,1,'laptop','laptop negru prafuit',sysdate,sysdate);
insert into items values(4,1,'scaun','scaun verde scartaie',sysdate,sysdate);
insert into items values(3,10,'cafea','cafea da energie ca sa nu mori',sysdate,sysdate);
insert into items values(2,9,'geanta','geanta cara chestii something',sysdate,sysdate);
insert into items values(1,8,'incarcator','something something',sysdate,sysdate);
insert into items values(6,7,'papuci','talpa verde',sysdate,sysdate);
insert into items values(7,5,'ochelari','ochelari prafuiti si plini de urme',sysdate,sysdate);

insert into categories values(1,'electrocasnice');
insert into categories values(2,'aparatura');
insert into categories values(3,'mancare');
insert into categories values(4,'obiecte');

insert into item_category values(1,12,3);
insert into item_category values(2,10,4);
insert into item_category values(3,10,4);
insert into item_category values(4,10,2);
insert into item_category values(4,5,2);
insert into item_category values(5,5,4);
insert into item_category values(6,4,4);
insert into item_category values(7,3,3);
insert into item_category values(8,2,4);
insert into item_category values(9,1,2);
insert into item_category values(10,1,4);
insert into item_category values(10,6,4);
insert into item_category values(10,7,4);


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

