import fire

from config import Config


def main(config_file, run_type='train', checkpoint=''):
    # pylint: disable=no-member
    config = Config(config_file)

    print(config)

    if run_type == 'train':
        from trainer import Trainer
        trainer = Trainer(
            dataset_dir=config.dataset_dir,
            generator_channels=config.generator_channels,
            discriminator_channels=config.discriminator_channels,
            nz=config.nz,
            style_depth=config.style_depth,
            lrs=config.lrs,
            betas=config.betas,
            eps=config.eps,
            phase_iter=config.phase_iter,
            weights_halflife=config.weights_halflife_images,
            batch_size=config.batch_size,
            n_cpu=config.n_cpu,
            opt_level=config.opt_level
        )
        trainer.run(
            log_iter=config.log_iter,
            checkpoint=checkpoint
        )
    elif run_type == 'inference':
        from inferencer import Inferencer
        inferencer = Inferencer(
            generator_channels=config.generator_channels,
            nz=config.nz,
            style_depth=config.style_depth,
        )
        inferencer.inference(n=8)
    else:
        raise NotImplementedError


if __name__ == '__main__':
    fire.Fire(main)
