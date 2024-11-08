from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from .models import Reviews

def createreview(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save() 
            return redirect("../..")
    else:
        form = ReviewForm()
    
    return render(request, "createreview.html", {"form": form})

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Reviews, id=review_id)
    
    if review.user == request.user:
        review.delete()
        return redirect('../../..') 