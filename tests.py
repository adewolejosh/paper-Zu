# from fastapi.testclient import TestClient

# from main import app

# client = TestClient(app)


# def test_get_paper():
#     response = client.get("/api/papers/6716304fe41056dca11316ee")
#     assert response.status_code == 404
#     assert response.json() == {
#         "title": "Sample Paper Title",
#         "paper_type": "previous_year",
#         "paper_time": 180,
#         "marks": 100,
#         "params": {
#             "board": "CBSE",
#             "grade": 10,
#             "subject": "Maths"
#         },
#         "tags": [
#             "algebra",
#             "geometry"
#         ],
#         "chapters": [
#             "Quadratic Equations",
#             "Triangles"
#         ],
#         "sections": [
#             {
#                 "questions": [
#                     {
#                         "question": "Solve the quadratic equation: x^2 + 5x + 6 = 0",
#                         "answer": "The solutions are x = -2 and x = -3",
#                         "type": "short",
#                         "question_slug": "solve-quadratic-equation",
#                         "reference_id": "QE001",
#                         "hint": "Use the quadratic formula or factorization method",
#                         "params": {}
#                     },
#                     {
#                         "question": "In a right-angled triangle, if one angle is 30°, what is the other acute angle?",
#                         "answer": "60°",
#                         "type": "short",
#                         "question_slug": "right-angle-triangle-angles",
#                         "reference_id": "GT001",
#                         "hint": "Remember that the sum of angles in a triangle is 180°",
#                         "params": {}
#                     }
#                 ],
#                 "section_type": "default",
#                 "marks_per_question": 5
#             }
#         ],
#         "created_at": "2024-10-21T09:06:18.070000",
#         "updated_at": "2024-10-21T09:06:18.070000"
#     }


# def test_create_papers():
#     response = client.post(
#         "/api/papers",
#         json={
#             "title": "Sample Paper Title",
#             "paper_type": "previous_year",
#             "paper_time": 180,
#             "marks": 100,
#             "params": {
#                 "board": "CBSE",
#                 "grade": 10,
#                 "subject": "Maths"
#             },
#             "tags": [
#                 "algebra",
#                 "geometry"
#             ],
#             "chapters": [
#                 "Quadratic Equations",
#                 "Triangles"
#             ],
#             "sections": [
#                 {
#                     "questions": [
#                         {
#                             "question": "Solve the quadratic equation: x^2 + 5x + 6 = 0",
#                             "answer": "The solutions are x = -2 and x = -3",
#                             "type": "short",
#                             "question_slug": "solve-quadratic-equation",
#                             "reference_id": "QE001",
#                             "hint": "Use the quadratic formula or factorization method",
#                             "params": {}
#                         },
#                         {
#                             "question": "In a right-angled triangle, if one angle is 30°, what is the other acute angle?",
#                             "answer": "60°",
#                             "type": "short",
#                             "question_slug": "right-angle-triangle-angles",
#                             "reference_id": "GT001",
#                             "hint": "Remember that the sum of angles in a triangle is 180°",
#                             "params": {}
#                         }
#                     ],
#                     "section_type": "default",
#                     "marks_per_question": 5
#                 }
#             ],
#             "created_at": "2024-10-21T09:06:18.070000",
#             "updated_at": "2024-10-21T09:06:18.070000"
#         },
#     )
#     assert response.status_code == 201
#     assert response.json() == {
#         "_id": ""
#     }
