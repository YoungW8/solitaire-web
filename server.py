from http.server import HTTPServer, SimpleHTTPRequestHandler

class Handler(SimpleHTTPRequestHandler):
    def guess_type(self, path):
        if path.endswith('.js.br'):
            return 'application/javascript'
        elif path.endswith('.wasm.br'):
            return 'application/wasm'
        elif path.endswith('.data.br'):
            return 'application/octet-stream'
        elif path.endswith('.symbols.json.br'):
            return 'application/octet-stream'
        return super().guess_type(path)

    def end_headers(self):
        path = self.path.split('?')[0]
        if path.endswith('.br'):
            self.send_header('Content-Encoding', 'br')
        elif path.endswith('.gz'):
            self.send_header('Content-Encoding', 'gzip')
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        super().end_headers()

HTTPServer(('', 8080), Handler).serve_forever()
