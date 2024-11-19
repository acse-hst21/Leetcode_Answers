import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views['id'] = views.loc[views['author_id'] == views['viewer_id'], 'author_id']
    views = views.sort_values(by=['id'])
    return views[['id']].dropna().drop_duplicates()
