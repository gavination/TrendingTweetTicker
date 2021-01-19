def evaluate_sentiment(sentiment, original_message, recipient_number):
    switcher = {
       "positive": "It's looking good! They just might make it after all!",
       "negative": "Things are looking rough. Time to start packing bags :(",
       "is_neutral": "Not much happening in this one. Kinda boring :| "
    }

    header = str(switcher.get(sentiment, None))

    result_msg = f"Hello from the KimYe Engine!- {header} - {original_message}"
    result = {
      "body": result_msg,
      "to": recipient_number
    }

    return result