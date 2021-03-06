from Backend.DBController.DBConnection import DBConnection


def simpleSearchPage(toBeSearched: str, page: str, db_handler: DBConnection) -> bytes:
        allresults = db_handler.execute(
                f"SELECT TO_CHAR(ITEM_ID), TO_CHAR(USER_ID), P_NAME, TO_CHAR(CATEGORY_ID), PICTURE, TO_CHAR(S_PRICE), TO_CHAR(S_DATE), TO_CHAR(END_DATE), DESCRIPTION FROM ITEMS WHERE LOWER(P_NAME) LIKE '%{toBeSearched}%'")

        print("all results:", len(allresults))

        resultPages = db_handler.getResultsInPagesOf(9)

        print("Result pages: ", resultPages)

        # firstName, lastName, email, _, country, city, tel, picLink = result

        pages = [page for page in resultPages if page]

        print("Pages:", pages)

        try:
                requestedPage = pages[int(page) - 1]
        except IndexError:
                return b'0!0!0!0!'

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
