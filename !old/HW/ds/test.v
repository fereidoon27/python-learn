module example(input c);
reg b = 1'b0;
reg [2:0] d = 3'b001;
initial
begin
#5 b <= 1'b1;
d <= d + 1;
end

initial
$monitor
endmodule