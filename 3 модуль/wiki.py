import wikipedia

def get_with_article(article):
    wikipedia.set_lang('ru')
    try:
        return wikipedia.summary(article)
    except wikipedia.WikipediaException:
        return 'Не найдена статья!'