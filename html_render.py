def render_html_table(data):
    html = "<html>\n"
    html += '''<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/purecss@3.0.0/build/pure-min.css" integrity="sha384-X38yfunGUhNzHpBaEBsWLO+A0HDYOQi8ufWDkZ0k9e0eXz/tH3II7uKZ9msv++Ls" crossorigin="anonymous">\n'''
    html += '''<meta name="viewport" content="width=device-width, initial-scale=1">\n'''
    html += "<table  class='pure-table pure-table-bordered'>\n"
    for row in data:
        html += "<tr>\n"
        for col in row:
            html += f"<td>{col}</td>\n"
        html += "</tr>\n"
    html += "</table>"
    return html