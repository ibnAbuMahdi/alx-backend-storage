#!/usr/bin/env python3
""" students average score """


if __name__ != "__main__":
    def top_students(mongo_collection):

        pipeline = [
            {
                "$addFields": {
                    "averageScore": {"$avg": "$topics.score"}
                }
            },
            {
                "$sort": {"averageScore": -1}
            }
        ]
        return list(mongo_collection.aggregate(pipeline)) 
