def validate_img_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.png', '.jpeg', '.bmp']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Nepodporovaný typ souboru.')

def validate_obj_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.split(value.name)[1]
    valid_extensions = ['.obj']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Zde lze nahrát pouze soubory .obj')

def validate_mtl_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.split(value.name)[1]
    valid_extensions = ['.mtl']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Zde lze nahrát pouze soubory .mtl')