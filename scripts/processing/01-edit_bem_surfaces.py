import os.path as op
import mne
import os
from scripts.processing.library.config import study_path, subjects_dir
import shutil
import subprocess

# The paths to Freesurfer reconstructions
subject = 'sub006'
bem_dir = op.join(study_path, 'subjects', subject, 'bem')
print(bem_dir)

subjects_dir = op.join(study_path, 'subjects')
print(subjects_dir)
plots = op.join(study_path, 'plots')


def fswatch():
    os.system("fswatch -1 /Users/ricklicona/Documents/GitHub/mne-biomag-group-demo/subjects/sub006/conv")


def check_surfaces(subject):
    # subject = "sub%03d" % subject_id
    print("**********************************************SUBJECT: ", subject)
    bem_surfaces = mne.viz.plot_bem(subject=subject, subjects_dir=subjects_dir,
                                    brain_surfaces='white', orientation='coronal')
    # bem_surfaces.show()
    plot_name = op.join(plots, "%s_BEM" % (subject))
    bem_surfaces.savefig(plot_name, format='eps')


def edit_bem_surfaces():
    conv_dir = op.join(study_path, 'subjects', subject, 'conv')
    os.makedirs(conv_dir, exist_ok=True)
    # Read the fixed surface
    coords, faces = mne.read_surface(op.join(conv_dir, 'outer_skull_fixed.obj'))

    # Backup the original surface
    shutil.copy(op.join(bem_dir, 'outer_skull.surf'),
                op.join(bem_dir, 'outer_skull_orig.surf'))

    # Overwrite the original surface with the fixed versionbem
    mne.write_surface(op.join(bem_dir, 'outer_skull.surf'), coords, faces,
                      overwrite=True)

    # os.system('open /Users/ricklicona/Documents/GitHub/mne-biomag-group-demo/plots/sub004_BEM')

    # Read the fixed surface, INNER SKULL
    coords, faces = mne.read_surface(op.join(conv_dir, 'inner_skull_fixed.obj'))

    # Backup the original surface
    shutil.copy(op.join(bem_dir, 'inner_skull.surf'),
                op.join(bem_dir, 'inner_skull_orig.surf'))

    # Overwrite the original surface with the fixed version
    mne.write_surface(op.join(bem_dir, 'inner_skull.surf'), coords, faces,
                      overwrite=True)

    # Read the fixed surface, OUTER SKIN
    coords, faces = mne.read_surface(op.join(conv_dir, 'outer_skin_fixed.obj'))

    # Backup the original surface
    shutil.copy(op.join(bem_dir, 'outer_skin.surf'),
                op.join(bem_dir, 'outer_skin_orig.surf'))

    # Overwrite the original surface with the fixed version
    mne.write_surface(op.join(bem_dir, 'outer_skin.surf'), coords, faces,
                      overwrite=True)
    check_surfaces(subject)


def voice(flag):
    if flag == 1:
        os.system("say Listo")
    else:
        os.system("say Error")


def start_listening():
    while True:
        os.system("say Escuchando")
        try:
            fswatch()
            os.system("say Procesando")
            edit_bem_surfaces()
            voice(flag=1)
        except:
            voice(flag=0)
            print("****************************SURFACES ERROR!!")
            start_listening()


start_listening()