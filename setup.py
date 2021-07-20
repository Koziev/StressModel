import io
import setuptools

setuptools.setup(
    name="stress_model",
    version="0.0.2",
    author="Ilya Koziev",
    author_email="inkoziev@gmail.com",
    description="Phonetic transcription of text",
    #long_description=long_description,
    #long_description_content_type="text/markdown",
    url="https://github.com/Koziev/StressModel",
    packages=setuptools.find_packages(),
    package_data={'stress_model': ['nn_stress.cfg', '*.py', 'stress_model/nn_stress.model/variables/variables*', 'stress_model/nn_stress.model/*.pb']},
    include_package_data=True,
)
