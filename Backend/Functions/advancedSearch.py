from Backend.DBController.DBConnection import DBConnection

_search_template = "TO_CHAR(ITEM_ID), TO_CHAR(USER_ID), P_NAME, TO_CHAR(CATEGORY_ID), PICTURE, TO_CHAR(S_PRICE), TO_CHAR(S_DATE), TO_CHAR(END_DATE), DESCRIPTION"

_constraint_types = {
        "CATEGORY"            : lambda val: f"CATEGORY_ID IN (SELECT CATEGORY_ID FROM CATEGORIES WHERE CATEGORY_NAME LIKE '%{val}%')",
        "NAME"                : lambda val: f"LOWER(P_NAME) LIKE '%{val}%'",
        "FABRICATIONLOCATION" : lambda val: f"ITEM_ID IN (SELECT ITEM_ID FROM TAGS WHERE CHARACTERISTIC_NAME LIKE 'FABRICATION_COUNTRY' AND LOWER(CHARACTERISTIC_VALUE) LIKE '%{val}%')",
        "FABRICATIONYEAR"     : lambda val: f"ITEM_ID IN (SELECT ITEM_ID FROM TAGS WHERE CHARACTERISTIC_NAME LIKE 'FABRICATION_YEAR' AND LOWER(CHARACTERISTIC_VALUE) LIKE '%{val}%' )",
        "CONDITION"           : lambda val: f"ITEM_ID IN (SELECT ITEM_ID FROM TAGS WHERE CHARACTERISTIC_NAME LIKE 'CONDITION' AND LOWER(CHARACTERISTIC_VALUE) LIKE '%{val}%')",
        "MATERIAL"            : lambda val: f"ITEM_ID IN (SELECT ITEM_ID FROM TAGS WHERE CHARACTERISTIC_NAME LIKE 'MATERIAL' AND LOWER(CHARACTERISTIC_VALUE) LIKE '%{val}%')",
        "COLOR"               : lambda val: f"ITEM_ID IN (SELECT ITEM_ID FROM TAGS WHERE CHARACTERISTIC_NAME LIKE 'COLOR' AND LOWER(CHARACTERISTIC_VALUE) LIKE '%{val}%')",
        "OTHER"               : lambda val: f"ITEM_ID IN (SELECT ITEM_ID FROM TAGS WHERE CHARACTERISTIC_NAME LIKE 'OTHER_SPEC' AND LOWER(CHARACTERISTIC_VALUE) LIKE '%{val}%')"
        }

def advancedSearchPage(page: str, tags: str, db_conn: DBConnection) -> bytes:

        tags = [constraint.split("~") for constraint in tags.split("?")]
        tags = {name : value for name, value in tags}

        query = f"SELECT {_search_template} FROM ITEMS"

        # CATEGORY
        # NAME
        # FABRICATIONLOCATION
        # FABRICATIONYEAR
        # CONDITION
        # MATERIAL
        # COLOR
        # OTHER
        for tag_name, tag_val in tags.items():
                if query == f"SELECT {_search_template} FROM ITEMS":
                        query += " WHERE "
                else:
                        query += " AND "

                query += _constraint_types[tag_name](tag_val)

        db_conn.execute(query)

        pages = db_conn.getResultsInPagesOf(9)
        pages = [page for page in pages if page]

        print("Pages:", pages)

        requestedPage = pages[int(page) - 1]

        print("RequestedPage", requestedPage)

        print('\n'.join('   |   '.join(row) for row in requestedPage))

        curPage = int(page)
        maxPage = len(pages)

        hasPrevPage = 1 if curPage > 1 else 0
        hasNextPage = 1 if curPage < maxPage else 0

        result = '!'.join((
                str(hasPrevPage),
                str(hasNextPage),
                str(curPage),
                str(maxPage),
                '#'.join(
                        '???'.join(row) for row in requestedPage
                        )
                ))

        print("RESULT:", result)

        return result.encode()