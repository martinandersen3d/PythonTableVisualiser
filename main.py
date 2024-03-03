from import_csv import read_csv
from html_render import render_html_table
from http_serve import serve_http
import webbrowser

def main():
    # Read CSV file
    csv_file_path = 'example.csv'  # Update with your CSV file path
    data = read_csv(csv_file_path)
    
    # Open browser after server starts
    # webbrowser.open('http://localhost:8000',2)
    webbrowser.open('http://localhost:8000')
    
    # Serve HTTP
    serve_http('localhost', 8000, data)  # Passing data to the HTTP server



if __name__ == "__main__":
    main()
