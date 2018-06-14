from Backend.DBController.DBConnection import DBConnection

_constraint_types = {
        "CATEGORY" : lambda val: f"CATEGORY_ID IN (SELECT CATEGORY_ID FROM CATEGORIES WHERE CATEGORY_NAME LIKE '%{val}%')",
        "NAME"     : lambda val: f"P_NAME LIKE '%{val}%'"
        }

def advancedSearchPage(page: str, tags: str, db_conn: DBConnection) -> bytes:

        tags = [constraint.split("~") for constraint in tags.split("?")]
        tags = {name : value for name, value in tags}

        query = "SELECT * FROM ITEMS"

        # CATEGORY
        # NAME
        # FABRICATIONLOCATION
        # FABRICATIONYEAR
        # CONDITION
        # MATERIAL
        # COLOR
        # OTHER
        for tag_name, tag_val in tags.items():
                if query == "SELECT * FROM ITEMS":
                        query += " WHERE "
                else:
                        query += " AND "

                query += _constraint_types[tag_name](tag_val)

        # TODO execute the select n shit
        db_conn.execute(query)

        pages = db_conn.getResultsInPagesOf(9)

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
                        '?'.join(row) for row in requestedPage
                        )
                ))

        print("RESULT:", result)

        return result.encode()