from flask import Flask, jsonify, request

app = Flask(__name__)

capitals = {
    'France': 'Paris',
    'Allemagne': 'Berlin',
    'Espagne': 'Madrid',
    'Italie': 'Rome'
}

@app.route('/api/capital', methods=['GET'])
def get_capital():
    country = request.args.get('country')
    if country in capitals:
        return jsonify({'capital': capitals[country]})
    else:
        return jsonify({'error': 'Pays non trouvé'})

if __name__ == '__main__':
    app.run(port=5000, debug=True)