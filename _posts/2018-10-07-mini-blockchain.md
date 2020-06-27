---
layout: post
title: Python mini-blockChain (Transaction,POW,mining)🍪
comments: true
category: [cryptoCurrency,]
tag: [Python, Flask, blockChain,]
excerpt_separator: <!-- more -->
---
<img alt="암호화폐!" width="125" align="left" style="padding: 0px 10px 0px 0px;" src="/images/post_img/20181007-00.png" >


<span id="start-ch">Here</span>, I will introduce a simple implement of the mining a coin, which is important process to lock the block-chain. The processes are, creating transaction data, hash calculation, and proof-of-work (POW). Those will finally lock the block at the end of the chain. this whole process will be generated through Flask Server.
<!-- more -->

<br><br><br>
# BLOCKCHAIN for DUMMIES
> Everybody talks these days about the Blockchain. Everybody. But ask somebody about it. They will have a hard time trying to explain to you what is Blockchain.

| <img src="/images/post_img/20181007-01.png" width="550"> |
|:----------------------------------------------:|
|[image ref.]: [Blockchain for dummies](https://goo.gl/nfdANj)|



<br><br>
# 0. INTRO 👋

I made some simple structure of blockchain, but this is not for the project, but for the own personal study, the better understanding how blockchain work in simple way.
So, please just refer it as one of many sample materials.



<br><br>

|　**Language**　|　**Library**　|　**Data form**　|　**Reference**　|
|:--------:|:--------:|:----:|:---------------------------------------------:|
|Python    |Flask     |JSON  |[https://goo.gl/M6XU5v](https://goo.gl/M6XU5v)|



<br><br>
# 1. HOW TO RUN

Run bash window on the target folder and type in 'python server.py'. Then the first block, index 1, will be automatically generated if there is no stored history file named **chain.json**.

regarding **chain.json** file, there's no chain.json at first. it is generated only if you like to. (I prepare 'write' menu on webpage)

When '**chain.json**', a written history file, exists, the block history will be restored autonomously. To avoid at first, I changed the file name to '**chain_old.json**', which has the several depth of block history.



<br><br>

| <img src="/images/post_img/20181007-02.png" width="550"> |
|:----------------------------------------------:|
|a |


<br><br>
# 2. HOW IT SHOWS

> 'http://localhost:5000' in browser



<br><br>

| <img src="/images/post_img/20181007-03.png" width="450"> |
|:----------------------------------------------:|
|a |



<br><br>
# 3. ABOUT JSON
In block_class, there're 3 json files.

> 1. **blcok.json** - the first intention, but to many hashs
> 2. **chains_old.json** - already described on the top.
> 3. **genesis.json** - Ethurium genesis block format, just refer to it

This is not exact as it can be, but just alludes coinbase transaction. Because it is compensation for mining, sender is nobody, recipient is randomly generated node ID and amount is set as 100, form of variable for mining reward.

{% highlight python linenos %}
    {
     "sender": "0",
     "recipient": "17460cdf96bc403ca792bf08a7f87d4d",
     "amount": 100
    }
{% endhighlight python linenos %}



<br><br>

| <img src="/images/post_img/20181007-04.png" width="250"> |
|:----------------------------------------------:|
|a  |


<br><br>
# 4. OTHERS
> As a beginner trying to bite a little dent on learning the blockchain technology, other constructive opinoins are always welcomed and let's make it together! 😏




<br><br>
# 5. REFERENCES
> 1. [Making Blockchain with Python ( Only available Part.1)](https://goo.gl/V2owrp)
> 1. [Python Blockchain (Create Block, Transaction, mining)](https://goo.gl/M6XU5v)



<br><br>
# 6. CODE PART
> The rest of code part is at [**onitonitonito/block_chain_study**](https://github.com/onitonitonito/block_chain_study)


{% highlight python linenos %}
"""
# BlockChain API with Python Flask server
"""
# import json
# from textwrap import dedent

from uuid import uuid4
from flask import (Flask, jsonify, request, render_template, redirect)
from block_class.block_chain import BlockChain


app = Flask(__name__)

# to create 32-bits UID - '11864aaa-d1b2-45af-9c5a-c21dda71c6fc'
node_identifier = str(uuid4()).replace("-", "")

bc = BlockChain()


@app.route("/", methods=["GET"])
def index():
    return render_template('./chain_help.html')


@app.route("/chains", methods=["GET"])
def full_chain():
    response = {
        "chain": bc.chain,
        "length": len(bc.chain),
    }

    return jsonify(response), 200


@app.route("/mine", methods=["GET"])
def mine():
    # To Calculate POW, depending on the previous hash (compensation=100)
    last_block = bc.last_block
    last_proof = last_block["proof"]

    proof = bc.proof_of_work(last_proof)
    conpensation = 100

    bc.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=conpensation)

    previous_hash = bc.hash(last_block)
    block = bc.new_block(proof, previous_hash)

    response = {
        "message":         "... new block forged! ...",
        "index":           block["index"],
        "transactions":    block["transactions"],
        "proof":           block["proof"],
        "previous_hash":   block["previous_hash"]
    }

    return jsonify(response), 200


@app.route("/transactions/new", methods=["GET", "POST"])
def new_transaction():
    # to write and show the sender, recipient, amount if exist
    if request.method == "POST":
        # values = request.get_json()

        sender = request.form["sender"]
        recipient = request.form["recipient"]
        amount = request.form["amount"]

        values = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount}

        required = ["sender", "recipient", "amount"]

        if not all(k in values for k in required):
            return "... missing values ...", 400

        index = bc.new_transaction(
            values["sender"],
            values["recipient"],
            values["amount"])

        response = {
            "message": "... Transaction will be added to Block {0}".format(index),
            "current TX": bc.current_transactions
        }
        return jsonify(response), 201

    else:
        return render_template("./new_TX.html"), 200


@app.route("/transactions", methods=["GET"])
def show_transaction():
    # In order to record in the block, query the collected, before
    response = bc.current_transactions
    return jsonify(response), 200


@app.route("/transactions/all", methods=["GET"])
def show_transaction_all():
    # all transaction details are extracted (mining compensation is excluded)
    echo = bc.show_all_transaction(bc.chain)
    echo = "<pre>" + echo + "</pre>"

    return echo

@app.route("/write", methods=["GET"])
def write_chains():
    # The block, collected so far is stored in the Json file.
    chains = bc.write_json()
    response = {
        "chains": chains,
        "message": "...  Writing whole chains to chains.json ..."
    }
    return jsonify(response), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
{% endhighlight python linenos %}
