def render_html_table(data):
    html = '''
    <html>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/purecss@3.0.0/build/pure-min.css" integrity="sha384-X38yfunGUhNzHpBaEBsWLO+A0HDYOQi8ufWDkZ0k9e0eXz/tH3II7uKZ9msv++Ls" crossorigin="anonymous">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    body{padding: 25px;}
    </style>
    <body>'''
    html += "<table  class='pure-table pure-table-bordered'>\n"
    # Adding header row
    html += "<thead><tr>\n"
    for header in data[0]:
        html += f"<th>{header}</th>\n"
    html += "</tr></thead>\n"
    
    # Adding data rows
    for row in data[1:]:
        html += "<tr>\n"
        for col in row:
            html += f"<td>{col}</td>\n"
        html += "</tr>\n"
    html += "</table>"
    html += "</body>\n"
    html += "</html>"
    return html