import re

def preprocess_expression(expression, last_result):
    expression = expression.lower().replace("ans", str(last_result))
    expression = expression.replace(" ", "")
    expression = re.sub(r'(\d)(\()', r'\1*\2', expression)
    expression = re.sub(r'(\))(\d)', r'\1*\2', expression)
    expression = re.sub(r'(\))(\left()', r'\1*\2', expression)
    return expression

def main():
    last_result = 0
    print("--- Smart Calculator ---")

    while True:
        user_input = input("calc > ").strip()

        if user_input.lower() in ['exit', 'quit']:
            break

        if not user_input:
            continue

        try:
            clean_expr = preprocess_expression(user_input, last_result)
            
            if not set(clean_expr).issubset(set("0123456789+-*/(). ")):
                print("Error: Invalid characters.")
                continue

            last_result = eval(clean_expr)
            
            if isinstance(last_result, float) and last_result.is_integer():
                last_result = int(last_result)
                
            print(f"Result: {last_result}")

        except ZeroDivisionError:
            print("Error: Division by zero.")
        except (SyntaxError, ValueError):
            print("Error: Invalid expression.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()