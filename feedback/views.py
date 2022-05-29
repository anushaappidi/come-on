from django.shortcuts import render
from .models import Question
from .models import Feedback
from user.models import Student, Teacher

subjects = ['MATHS', 'PHYSICS', 'CHEMISTRY']
questions = Question.objects.all()


def feedback_form(request):
    context = {}

    if request.method == 'POST':

        for subject in subjects:
            feedback = Feedback()
            feedback.entry_by = Student.objects.get(
                student_name__pk=request.user.id)
            feedback.subject = subject
            marks_awarded = []
            for question in questions:
                marks_awarded.append(int(request.POST[subject + "_" +
                                                  question.Quality]))
            dummy = {'Marks': marks_awarded}
            feedback.answers = dummy
            feedback.save()
            return render(request,'feedback/base.html')

        # print(request.user.id)
        # print(request.POST["MATHS_clears all doubts"])

    else:
        context = {'subjects': subjects, 'questions': questions}
    return render(request, 'feedback/feedback_form.html', context)


# Create your views here.


def feedback(request):
    current_teacher = Teacher.objects.get(teacher_name__pk=request.user.id)
    subject_of_teacher = current_teacher.subject
    subject_data = Feedback.objects.filter(subject=subject_of_teacher).values()
    no_of_qualities = questions.count()
    final_answers = [0] * no_of_qualities
    for tuple in subject_data:
        marks_for_subject = tuple['answers']['Marks']
        for i in range(no_of_qualities):
            final_answers[i] += marks_for_subject[i]

    qualities = []
    data = []

    # data_json = {
    #     subject_of_teacher: subject_of_teacher,
    # }
    # for i in range(no_of_qualities):
    #     key = questions[i].Quality
    #     value = final_answers[i]
    #     data_json[key] = value
    #     qualities.append(questions[i].Quality)

    
    for i in range(no_of_qualities):
        data_json = {}
        key = questions[i].Quality
        value = final_answers[i]
        data_json[key] = value
        qualities.append(questions[i].Quality)
        data_json["quality"] = key
        data.append(data_json)

    # data = [data_json]

    chart_data = {
        "element":
        "bar-chart",
        "data":
        data,
        "xkey":
        "quality",
        "barSizeRatio":
        0.70,
        "barGap":
        3,
        "resize":
        True,
        "responsive":
        True,
        "ykeys":
        qualities,
        "labels":
        qualities,
        "barColors": [
            "0-#1de9b6-#1dc4e9", "0-#899FD4-#A389D4", "#04a9f5",
            "0-#1de9b6-#1dc4e9", "0-#899FD4-#A389D4"
        ]
    }
    context = {'chart_data': chart_data}

    return render(request, 'feedback/feedback.html', context)

def base(request):
    return render(request, 'feedback/base.html')

