from import_csv import read_csv
from html_render import render_html_table
from http_serve import serve_http

def main():
    # Read CSV file
    csv_file_path = 'example.csv'  # Update with your CSV file path
    data = read_csv(csv_file_path)

    # Serve HTTP
    serve_http('localhost', 8000, data)  # Passing data to the HTTP server

if __name__ == "__main__":
    main()
