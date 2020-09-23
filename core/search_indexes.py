from haystack import indexes
from .models import Video

class VideoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    video_description = indexes.CharField(model_attr='video_description')
    video_title = indexes.CharField(model_attr='video_title')
    video_owner = indexes.CharField(model_attr='video_owner')
    
    def get_model(self):
        return Video

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
