FROM stevenshin/ssyprojectbackend-ubuntu-python3.6-django-uwsgi:latest
LABEL version "ssyproject backend api uwsgi setting"
LABEL description "ssyproject backend api uwsgi setting"

# RUN echo "source activate specialenv" > ~/.bashrc
# ENV PATH /opt/anaconda3/envs/specialenv/bin:$PATH

# ENV BASH_ENV ~/.bashrc
# SHELL ["/bin/bash", "-c"]
# RUN conda activate specialenv
# # RUN echo "conda activate my-env" >> ~/.bashrc
# CMD ["uwsgi", "/workspace/specialapiproject/config/uwsgi/uwsgi-special.ini"]

# RUN echo "source /opt/conda/etc/profile.d/conda.sh"
# RUN echo "conda activate specialenv" >> ~/.bashrc

RUN echo "uwsgi /workspace/ssyprojectbackend/config/uwsgi/uwsgi-ssyprojectbackend.ini" >> /root/.bashrc

RUN pip install django-storages && \
    pip install boto3

CMD ["/bin/bash"]

# CMD ["uwsgi", "/workspace/specialapiproject/config/uwsgi/uwsgi-special.ini"]
    
# CMD ["uwsgi"]