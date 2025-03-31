module tb_q3_2 ;

reg clk,reset,load,up_down;
reg [3:0] data;
wire [3:0] count;

// Control the clk signal that drives the design block.
initial clk = 1'b0;
always #5 clk = ~clk;

// instantiate the design block
counter counter1 (clk,reset,up_down,load,data,count);

initial 
begin
// assigning
end

initial
$monitor($time, " output count is %d ", count);

endmodule