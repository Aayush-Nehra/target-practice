import pygame

def _get_scaled_image(path, scale=1):
    """Loads a scaled image without empty pixels"""
    image = pygame.transform.scale_by(
        pygame.image.load(path).convert_alpha(),scale) 
    rect = image.get_bounding_rect()
    trimmed_image = pygame.Surface(rect.size, pygame.SRCALPHA)
    trimmed_image.blit(image,(0,0),rect)
    return trimmed_image