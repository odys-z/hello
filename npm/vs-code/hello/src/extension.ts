// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import path = require('path');
import * as vscode from 'vscode';
import * as cp from "child_process";


// this method is called when your extension is activated
// your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {
	
	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Congratulations, your extension "hello" is now active!');

	// The command has been defined in the package.json file
	// Now provide the implementation of the command with registerCommand
	// The commandId parameter must match the command field in package.json
	let disposable = vscode.commands.registerCommand('hello.hi', () => {
		// The code you place here will be executed every time your command is executed
		// Display a message box to the user
		vscode.window.showInformationMessage('Hello VS Code Extension from Hello!!');
	});

	context.subscriptions.push(disposable);

	disposable = vscode.commands.registerCommand('hello.py', () => {
		let scriptpath = context.asAbsolutePath(path.join('res', 'anserv.py'));

		function getDocumentWorkspaceFolder(): string | undefined {
			const fileName = vscode.window.activeTextEditor?.document.fileName;
			return vscode.workspace.workspaceFolders
				?.map((folder) => folder.uri.fsPath)
				.filter((fsPath) => fileName?.startsWith(fsPath))[0];
		}
		let fullFilePath = context.asAbsolutePath(path.join('res', 'anserv.py'));
		let cmd = `pwd && python3 ${fullFilePath} -w ${getDocumentWorkspaceFolder()} &`;
		console.log(cmd);
		vscode.window.showInformationMessage(cmd);
		new Promise<string>((resolve, reject) => {
			cp.exec(cmd, (err, out) => {
				if (err) {
					vscode.window.showInformationMessage(err.message);
					return reject(err);
				}
				vscode.window.showInformationMessage('ok');
				return resolve(out);
			});
		});
	});

	context.subscriptions.push(disposable);

}

// this method is called when your extension is deactivated
export function deactivate() {}
