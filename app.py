from flask import Flask, request, jsonify

app = Flask(__name__)

def categorize_person(age, gender):
    if age > 22:
        if gender.lower() == "male":
            return "Male Employee!"
        elif gender.lower() == "female":
            return "Female Employee!"
    else:
        if gender.lower() == "male":
            return "Male Intern!"
        elif gender.lower() == "female":
            return "Female Intern!"
    return "Invalid input!"

@app.route('/categorize', methods=['POST'])
def categorize():
    data = request.get_json()
    
    if 'age' not in data or 'gender' not in data:
        return jsonify({"error": "Please provide both age and gender"}), 400

    try:
        age = int(data['age'])
        gender = data['gender']
        result = categorize_person(age, gender)
        return jsonify({"category": result})
    except ValueError:
        return jsonify({"error": "Invalid age format"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
