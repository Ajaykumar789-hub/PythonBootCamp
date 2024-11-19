from collections import defaultdict

def transaction_passes(risk_service, labels):
    # Extract data
    user_ids = risk_service["user_id"]
    txn_ids = risk_service["txn_id"]
    statuses = risk_service["status"]
    
    label_user_ids = labels["user_id"]
    label_txn_ids = labels["txn_id"]
    label_names = labels["label_name"]
    
    # Step 1: Filter transactions with "pass" status
    pass_transactions = defaultdict(list)
    for i in range(len(user_ids)):
        if statuses[i] == "pass":
            pass_transactions[user_ids[i]].append(txn_ids[i])
    
    # Step 2: Identify users with more than one "pass"
    result = []
    for user_id, transactions in pass_transactions.items():
        if len(transactions) > 1:
            # Find associated labels for the user
            user_labels = [label_names[i] for i in range(len(label_user_ids)) if label_user_ids[i] == user_id]
            unique_labels = set(user_labels)
            
            if len(unique_labels) == 1:
                # All labels are the same; return one record
                result.append((user_id, list(unique_labels)[0]))
            else:
                # Labels are different; return multiple records
                for label in unique_labels:
                    result.append((user_id, label))
    
    return result

# Example input
risk_service = {
    "user_id": [6, 4, 6, 5, 2, 5, 3, 6, 1, 6, 7],
    "txn_id": [12, 11, 10, 9, 8, 7, 6, 5, 4, 10, 11],
    "event_datetime": ['1/6/16', '1/4/16', '1/6/16', '1/5/16', '1/2/16', 
                       '1/1/16', '1/6/16', '1/6/16', '1/1/16', '1/6/16', '1/1/16'],
    "status": ['pass', 'pass', 'block', 'pass', 'pass', 
               'pass', 'block', 'pass', 'block', 'pass', 'pass']
}

labels = {
    "user_id": [1, 1, 3, 4, 5, 6, 6, 5, 6, 3, 6, 4],
    "txn_id": [2, 6, 7, 9, 8, 12, 3, 5, 1, 4, 10, 11],
    "label_name": ['Synthetic', 'ATO', 'Synthetic', 'Synthetic', 
                   'Synthetic', 'ATO', 'Synthetic', 'Synthetic', 
                   'ATO', 'Synthetic', 'ATO', 'Synthetic'],
    "label_date": [42929, 43038, 43049, 43322, 43052, 
                   43371, 43008, 43021, 42899, 43018, 43340, 43353]
}

# Example usage
print(transaction_passes(risk_service, labels))
