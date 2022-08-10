table_rows = table.find_all('tr')
    res = []
    
    for tr in table_rows:
        td = tr.find_all('td')
        row = [tr.text.strip() for tr in td if tr.text.strip()]
        if row:
            res.append(row)
            
    df = pd.DataFrame(res, columns=[])
    print(df)
