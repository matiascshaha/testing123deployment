from flask import Flask, request, jsonify
from src.schema import schema  # Import your existing schema

# Initialize Flask App
app = Flask(__name__)


# Define the /graphql endpoint manually
@app.route("/graphql", methods=["POST"])
def graphql_server():
    # Get the JSON data from the incoming request
    data = request.get_json()

    # Execute the GraphQL query using the schema imported from app/schema.py
    result = schema.execute(
        data.get("query"),
        variables=data.get("variables"),
        context_value=request,
        operation_name=data.get("operationName")
    )

    # Prepare and return the response
    response = {"data": result.data}
    if result.errors:
        response["errors"] = [str(error) for error in result.errors]
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
