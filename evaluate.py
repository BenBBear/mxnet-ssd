import argparse
import tools.find_mxnet
import mxnet as mx
import os
import sys
from evaluate.evaluate_net import evaluate_net

def parse_args():
    parser = argparse.ArgumentParser(description='Evaluate a network')
    parser.add_argument('--dataset', dest='dataset', help='which dataset to use',
                        default='pascal', type=str)
    parser.add_argument('--year', dest='year', help='can be 2007, 2010, 2012',
                        default='2007', type=str)
    parser.add_argument('--eval-set', dest='eval_set', type=str, default='test',
                        help='evaluation set')
    parser.add_argument('--devkit-path', dest='devkit_path', help='VOCdevkit path',
                        default=os.path.join(os.getcwd(), 'data', 'VOCdevkit'), type=str)
    parser.add_argument('--network', dest='network', type=str, default='vgg16_reduced',
                        choices=['vgg16_reduced'], help='which network to use')
    parser.add_argument('--batch-size', dest='batch_size', type=int, default=32,
                        help='evaluation batch size')
    parser.add_argument('--epoch', dest='epoch', help='epoch of pretrained model',
                        default=112, type=int)
    parser.add_argument('--prefix', dest='prefix', help='new model prefix',
                        default=os.path.join(os.getcwd(), 'model', 'ssd'), type=str)
    parser.add_argument('--gpu', dest='gpu_id', help='GPU device to train with',
                        default=0, type=int)
    parser.add_argument('--cpu', dest='cpu', help='use cpu to evaluate',
                        action='store_true')
    parser.add_argument('--data-shape', dest='data_shape', type=int, default=300,
                        help='set image shape')
    parser.add_argument('--mean-r', dest='mean_r', type=float, default=123,
                        help='red mean value')
    parser.add_argument('--mean-g', dest='mean_g', type=float, default=117,
                        help='green mean value')
    parser.add_argument('--mean-b', dest='mean_b', type=float, default=104,
                        help='blue mean value')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    ctx = mx.cpu() if args.cpu else mx.gpu(args.gpu_id)
    evaluate_net(args.network, args.dataset, args.devkit_path,
                 (args.mean_r, args.mean_g, args.mean_b), args.data_shape,
                 args.prefix, args.epoch, ctx, year=args.year,
                 sets=args.eval_set, batch_size=args.batch_size)
