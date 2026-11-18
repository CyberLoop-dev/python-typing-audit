#!/usr/bin/env python3
"""Audit Python functions for missing argument and return annotations."""
import argparse
import ast
import json
from pathlib import Path

IGNORED_DIRS={".git","__pycache__",".venv","venv","node_modules","dist","build"}


def audit_source(source: str, filename: str = "<string>") -> list[dict]:
    tree=ast.parse(source,filename=filename)
    findings=[]
    for node in ast.walk(tree):
        if not isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef)):
            continue
        arguments=list(node.args.posonlyargs)+list(node.args.args)+list(node.args.kwonlyargs)
        if node.args.vararg: arguments.append(node.args.vararg)
        if node.args.kwarg: arguments.append(node.args.kwarg)
        for arg in arguments:
            if arg.arg in {"self","cls"}:
                continue
            if arg.annotation is None:
                findings.append({"file":filename,"line":arg.lineno,"function":node.name,"kind":"argument","name":arg.arg})
        if node.name!="__init__" and node.returns is None:
            findings.append({"file":filename,"line":node.lineno,"function":node.name,"kind":"return","name":"return"})
    return sorted(findings,key=lambda item:(item["line"],item["kind"],item["name"]))


def collect_files(target: Path) -> list[Path]:
    if target.is_file():
        return [target] if target.suffix==".py" else []
    return sorted(p for p in target.rglob("*.py") if not any(part in IGNORED_DIRS for part in p.parts))


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path",type=Path)
    parser.add_argument("--json",action="store_true",dest="as_json")
    parser.add_argument("--strict",action="store_true",help="exit 1 when any missing annotation is found")
    args=parser.parse_args()
    if not args.path.exists():
        parser.error(f"path does not exist: {args.path}")
    findings=[]
    for file in collect_files(args.path):
        try:
            findings.extend(audit_source(file.read_text(encoding="utf-8"),str(file)))
        except (OSError,SyntaxError) as exc:
            print(f"SKIP {file}: {exc}")
    if args.as_json:
        print(json.dumps(findings,indent=2))
    elif not findings:
        print("No missing function annotations found.")
    else:
        for item in findings:
            print(f"{item['file']}:{item['line']}: {item['function']} — missing {item['kind']} annotation for {item['name']}")
        print(f"\n{len(findings)} finding(s).")
    return 1 if args.strict and findings else 0


if __name__=="__main__":
    raise SystemExit(main())
