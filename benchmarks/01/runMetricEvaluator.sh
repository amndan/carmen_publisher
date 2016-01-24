#!/bin/bash

DATA="intel"
BAGS="../../bags/slamBenchmarking"
EVAL="../../metricEvaluator/metricEvaluator"

$EVAL \
-s ./test.log \
-r $BAGS/$DATA.relations \
-o $BAGS/$DATA.clf -w "{1.0,1.0,0.0,0.0,0.0,0.0}" \
-e stdVarTrans.errors -e2 sorted2ndTsTrans.errors

$EVAL \
-s ./test.log \
-r $BAGS/$DATA.relations \
-o $BAGS/$DATA.clf -w "{0.0,0.0,0.0,0.0,0.0,1.0}" \
-e stdVarPhi.errors -e2 sorted2ndTsPhi.errors

echo "set terminal wxt 0" > graph.gnuplot
echo "plot 'sorted2ndTsTrans.errors' w points" >> graph.gnuplot
echo "set terminal wxt 1" >> graph.gnuplot
echo "plot 'sorted2ndTsPhi.errors' w points" >> graph.gnuplot
echo "pause -1" >> graph.gnuplot
echo "Hit return to exit"

gnuplot graph.gnuplot

exit 0


