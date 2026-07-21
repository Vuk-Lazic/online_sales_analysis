import pandas as pd
import numpy as np

def convert_to_numeric(df):
    df['times_borrowed'] = df['times_borrowed'].astype('Int32')
    df['page_count'] = df['page_count'].astype('Int32')
    df['total_copies'] = pd.to_numeric(df['total_copies'], errors='coerce')
    df['total_copies'] = df['total_copies'].astype('Int16')
    df['year_published'] = pd.to_numeric(df['year_published'], errors='coerce')
    df['year_published'] = df['year_published'].astype('Int16')
    return df

def convert_to_datetime(df):
    df['last_borrowed_date'] = pd.to_datetime(
        df['last_borrowed_date'], format='%d_%b_%y', errors='coerce')
    return df

def convert_to_category(df):
    df['genre'] = df['genre'].astype('category')
    df['section'] = df['section'].astype('category')
    df['language'] = df['language'].astype('category')
    return df

def parse_rating(text):
    if pd.isna(text) or str(text).strip().lower() == "no rating available":
        return np.nan
     
    parts = str(text).split()                                                   
     
    try:
        return float(parts[0])     
    except (ValueError, IndexError):
        return np.nan


def parse_ratings_count(text):
    if pd.isna(text) or str(text).strip().lower() == "no reviews":
        return np.nan
    parts = str(text).replace(',', '').split()                                      
    try:
        return int(parts[0])
    except (ValueError, IndexError):
        return np.nan
    
def parse_price(text):
    if pd.isna(text) or str(text).strip().lower() == "price not available":
        return np.nan 
    try:
        price_str = str(text).replace('$', '').strip()                                 
        return float(price_str)
    except ValueError:
        return np.nan
    
def extract_numerical_values(df):
    df['rating'] = df['rating'].apply(parse_rating)
    df['ratings_count'] = df['ratings_count'].apply(parse_ratings_count)
    df['price'] = df['price'].apply(parse_price)
    
    return df

def extract_dimensions_features(df):
    df[['dimensions_width', 'dimensions_thickness', 'dimensions_height']] = df['dimensions'].str.replace(
        "inches", "").str.replace(" ", "").str.split('x', expand=True).astype(float)
    
    return df.drop('dimensions', axis=1)

def extract_catalog_position_features(df):
    df[['catalog_shelf', 'catalog_row', 'catalog_row_number']] = df['catalog_position'].str.split('-', expand=True)
    return df

def handle_missing_values(df):
    df.dropna(axis = 1, thresh = (df.shape[0]*0.75), inplace = True)
    df.dropna(axis = 0, thresh = df.shape[1] - 18,inplace = True)
    df.dropna(subset = ['catalog_position', 'title', 'author'], how = 'all', inplace = True)
    df['title'] = df['title'].fillna("Unknown Title")
    df['author'] = df['author'].fillna("Unknown Author")
    
    return df

def duplicate_data(df):
    df.drop_duplicates(keep = 'first', inplace = True, ignore_index = False)
    return df

def validate_data(df):
    mask = (df['times_borrowed'] == 0) & (df['last_borrowed_date'].notna() | df['rating'].notna() | df['ratings_count'].notna())
    df.loc[mask, 'last_borrowed_date'] = pd.NaT
    df.loc[mask, 'rating'] = np.nan                                 
    df.loc[mask, 'ratings_count'] = np.nan
    
    mask = (df['ratings_count'].isna()) & (df['rating'].notna())              
    df.loc[mask, 'rating'] = np.nan
    
    return df

def data_standardization(df):
    mapping = {
    'eng': 'en',
    'En': 'en',
    "pt-BR": "br",
    "zh-CN": "cn"
    }
    df['language'] = df['language'].astype(object).replace(mapping).astype("category")
    
    mapping = {
    'Young Adult (YA)': 'Young Adult',
    "Children's": "Children",
    "Children's Fiction": "Children"
    }
    df['section'] = df['section'].astype(object).replace(mapping).astype("category")
    
    mapping = {
    'Lev Tolstoy': 'Leo Tolstoy',
    'Winston S. Churchill': 'Winston Churchill',                            
    'Plato': 'Platon',
    'Will Shakespeare': 'William Shakespeare'
    }
    df['author'] = df['author'].replace(mapping)
    
    return df

def prepare_data(df):
    return df.pipe(convert_to_numeric).pipe(convert_to_datetime).pipe(convert_to_category).pipe(extract_numerical_values).pipe(extract_dimensions_features).pipe(extract_catalog_position_features).pipe(handle_missing_values).pipe(duplicate_data).pipe(validate_data).pipe(data_standardization)
    
