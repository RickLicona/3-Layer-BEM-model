from scripts.processing.library.config import exclude_subjects


subject_id=1

while subject_id < 20:
    if subject_id not in exclude_subjects:
        print("good: ", subject_id)
        subject_id+=1
    else:
        print("bad: ", subject_id)
        subject_id += 1
