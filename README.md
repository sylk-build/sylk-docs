# sylk-docs

This project has been generated thanks to [```sylk.build```](https://www.sylk.build) !

This project is using gRPC as main code generator and utilize HTTP2 + protobuf protocols for communication.

# Overview

Sylk plugin for auto-generated docs with [`docusaurus-sylk`](https://www.npmjs.com/package/docusaurus-sylk) plugin for [`Docusaurus`](https://docusaurus.io/).

This plugin built with [`Pluggy`](https://pluggy.readthedocs.io/en/stable/) and implement [`sylk.builder.hookimpl`](https://github.com/sylk-build/sylk/blob/main/sylk/builder/src/hookspecs.py) hookspec to be called from sylk cli build process.

# Features

This plugin provide the following features:

- Auto generated docs with [Docosaurus](https://docusaurus.io/) based on [`sylk schema`](https://docs.sylk.build/cli/resources/intro)
- Beautiful documentation based on [`Envoy`](https://www.envoyproxy.io/) theme
- Easy sidebar navigation
- Links references within the documentation all automatically resolves to relevant docs


# Usage

This plugin project is meant to be used __ONLY__ with [`Sylk CLI`](https://sylk.build/).

1. First install Sylk CLI with the extra provided for [sylk-docs](https://github.com/sylk-build/sylk-docs) dependencies:
```sh
pip install sylk[docs]
```
2. Create a new project
```sh
sylk new AwesomeDocs
cd AwesomeDocs
```
3. There you will find `sylk.json` file open it and enter the following configs under `configs.plugins` array and `project.extensions` array:

```json
{
  // ... more above ...
  "configs": {
    // ... more options ...
	"plugins": [
		"sylk-docs"
	]
  },
  "project": {
    // ... more properties above ...
    "extensions": [
	  {
	    "@type": "sylk-docs/sylk.Plugin.v1.Plugin",
		"docusaurus": {
		  "sylk": {
		    "sylkJsonPaths": [
			  "./sylk/AwesomeDocs/sylk.json"
		    ],
		    "sylkDocsPath": "./sylkdocs",
		    "sidebarPath": "./sidebarsSylkdocs.js"
		  },
		  "docs": {
		    "routeBasePath": "sylkdocs",
		    "sidebarPath": "./sidebarsSylkdocs.js"
		  }
	    }
	  }
    ]
  }
}
```

4. Create your project schema resources [`Quick Guide`](https://docs.sylk.build/cli/quick-start) to sylk CLI
5. When you are ready build the project resources with [`sylk build`](https://docs.sylk.build/cli/commands#build) command, this will run the plugin as well in the build lifecycle and will instantiate / re-build the project docs

# Index
Usage:
- [Python](#python)

Resources:
- [docs](#docs)
- [Plugin](#plugin)
- [Docusaurus](#docusaurus)
- [Readme](#readme)

# Services

## docs

__`build`__ [Unary]
- Input: [sylk.Docusaurus.v1.PresetOptions](#presetoptions)
- Output: [google.protobuf.Empty](#empty)

# Packages

## `sylk.Plugin.v1`


<details id="#Plugin">
<summary><b>Plugin</b></summary>

### __Plugin__
: 
* __readme__ [[Markdown](#Markdown)]


* __docusaurus__ [[PresetOptions](#PresetOptions)]

</details>

## `sylk.Docusaurus.v1`


<details id="#PresetOptions">
<summary><b>PresetOptions</b></summary>

### __PresetOptions__
: 
* __sylk__ [[PluginOptions](#PluginOptions)]


* __docs__ [[ContentDocOptions](#ContentDocOptions)]

</details>


<details id="#PluginOptions">
<summary><b>PluginOptions</b></summary>

### __PluginOptions__
: 
* __sylkJsonPaths__ [TYPE_STRING]


* __sylkDocsPath__ [TYPE_STRING]


* __sidebarPath__ [TYPE_STRING]


* __routeBasePath__ [TYPE_STRING]


* __git__ [TYPE_STRING]

</details>


<details id="#ContentDocOptions">
<summary><b>ContentDocOptions</b></summary>

### __ContentDocOptions__
: 
* __routeBasePath__ [TYPE_STRING]


* __sidebarPath__ [TYPE_STRING]

</details>

## `sylk.Readme.v1`


<details id="#Markdown">
<summary><b>Markdown</b></summary>

### __Markdown__
: 
* __path__ [TYPE_STRING]


* __title__ [TYPE_STRING]

</details>


# Usage

This project supports clients communication in the following languages:

### Python

```py
from clients.python import sylkdocs

client = sylkdocs()

# Unary call
response = stub.<Unary>(<InMessage>())
print(response)

# Server stream
responses = stub.<ServerStream>(<InMessage>())
for res in responses:
	print(res)

# Client Stream
requests = iter([<InMessage>(),<InMessage>()])
response = client.<ClientStream>(requests)
print(response)

# Bidi Stream
responses = client.<BidiStream>(requests)
for res in responses:
	print(res)
```


* * *
__This project and README file has been created thanks to [sylk.build](https://www.sylk.build)__