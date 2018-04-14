
% http://www.matrixlab-examples.com/impulse-function.html

%function y = dirac(n)
%    y = 0;
%    if n == 0
%        y = 1;
%    end
%end

function y = dirac(f)
    y = zeros(1, length(f))
    y(find(f==0)) == 1
end

n = -12:12;
%x = sin(n);
f = 4*dirac(n) + 3*dirac(n-2);
stem(n,f);
xlabel('n');
ylabel('Impulse function');
pause();
