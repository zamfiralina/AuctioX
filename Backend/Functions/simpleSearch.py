from Backend.DBController.DBConnection import DBConnection


def simpleSearchPage(toBeSearched: str, page: str, db_handler: DBConnection) -> bytes:
        allresults = db_handler.execute(
                f"SELECT TO_CHAR(ITEM_ID), TO_CHAR(USER_ID), P_NAME, TO_CHAR(CATEGORY_ID), PICTURE, TO_CHAR(S_PRICE), TO_CHAR(S_DATE), TO_CHAR(END_DATE), DESCRIPTION FROM ITEMS WHERE P_NAME LIKE '%{toBeSearched}%'")

        resultPages = db_handler.getResultsInPagesOf(9)

        print("Result pages: ", resultPages)

        # firstName, lastName, email, _, country, city, tel, picLink = result

        pages = [page for page in resultPages if page]

        print("Pages:", pages)

        # requestedPage = resultPages[int(page)-1]

        requestedPage = pages[int(page) - 1]

        print("RequestedPage", requestedPage)

        print('\n'.join('   |   '.join(row) for row in requestedPage))

        curPage = int(page)
        maxPage = len(pages)

        hasNextPage = 1 if curPage < maxPage else 0
        hasPrevPage = 1 if curPage is not 0 else 0

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
