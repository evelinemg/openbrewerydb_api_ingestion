base_url="https://api.openbrewerydb.org/v1/breweries"

dtypes = {'id': int,
          'brewery_type': 'category',
          'state': 'category',
          'country': 'category',
          'latitude': float,
          'longitude': float,
          }

params = {'page':0,
          'per_page':200}