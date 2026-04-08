import sys
import argparse
import operator

def cli_calculator():
    parser = argparse.ArgumentParser(
        description='CLI Calculator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s add 5 3
  %(prog)s divide 10 3 -p 4
  %(prog)s power 2 8
  %(prog)s mod 17 5
  %(prog)s "5 + 3 * 2"  # Expression mode
        '''
    )
    
    # Support both modes: operation mode and expression mode
    parser.add_argument(
        'expression',
        nargs='+',
        help='Operation and numbers, or quoted expression'
    )
    parser.add_argument('-p', '--precision', type=int, default=2)
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-q', '--quiet', action='store_true', help='Suppress all output except result')
    
    args = parser.parse_args()
    
    # If single argument, treat as expression
    if len(args.expression) == 1:
        try:
            # Simple eval (in production, use a proper expression parser)
            result = eval(args.expression[0])
            print(f"{result:.{args.precision}f}")
            sys.exit(0)
        except Exception as e:
            print(f"Error: Invalid expression - {e}", file=sys.stderr)
            sys.exit(1)
    
    # Otherwise, traditional operation mode
    if len(args.expression) != 3:
        print("Error: Expected format: operation num1 num2", file=sys.stderr)
        sys.exit(1)
    
    op_name, num1_str, num2_str = args.expression
    
    operations = {
        'add': operator.add,
        'sub': operator.sub,
        'subtract': operator.sub,
        'mul': operator.mul,
        'multiply': operator.mul,
        'div': operator.truediv,
        'divide': operator.truediv,
        'pow': operator.pow,
        'power': operator.pow,
        'exp': operator.pow,
        'mod': operator.mod,
        'modulus': operator.mod,
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.pow,
        '%': operator.mod,
    }
    
    if op_name not in operations:
        print(f"Error: Unknown operation '{op_name}'", file=sys.stderr)
        print(f"Valid operations: {', '.join(sorted(set(operations.keys())))}", file=sys.stderr)
        sys.exit(1)
    
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        print("Error: Invalid numbers", file=sys.stderr)
        sys.exit(1)
    
    if op_name in ['div', 'divide', '/'] and num2 == 0:
        print("Error: Division by zero", file=sys.stderr)
        sys.exit(1)
    
    if op_name in ['mod', 'modulus', '%'] and num2 == 0:
        print("Error: Modulus by zero", file=sys.stderr)
        sys.exit(1)
    
    result = operations[op_name](num1, num2)
    
    if not args.quiet:
        if args.verbose:
            symbol_map = {
                'add': '+', 'subtract': '-', 'sub': '-',
                'multiply': '*', 'mul': '*',
                'divide': '/', 'div': '/',
                'power': '**', 'pow': '**', 'exp': '**',
                'modulus': '%', 'mod': '%'
            }
            symbol = op_name if op_name in '+-*/**%' else symbol_map.get(op_name, op_name)
            print(f"{num1} {symbol} {num2} = {result:.{args.precision}f}")
        else:
            print(f"{result:.{args.precision}f}")
    else:
        print(result)
    
    sys.exit(0)

if __name__ == "__main__":
    cli_calculator()