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
                       
                       
                       

                       




